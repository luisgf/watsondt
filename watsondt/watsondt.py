#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

    apt-get install zlib1g-dev libxslt-dev libxml2 libxml2-dev tshark

"""

import argparse, sys

from ioc import genera_ioc
from procesos import Procesos, Estado
from blacklists import BlackLists
from colores import fail, ok, bold
from pcapcapture import PcapCapture
from conexiones import ConexManager, Conexion
from ioccybox import Cybox
from incibe import IncibeAntibotNet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Watson Detection Tool')
    parser.add_argument('-c', '--show-conn', action='store_true',
                        help='Muestra SOLO procesos con conexiones')
    parser.add_argument('-p', '--generate-profile',
                        choices=['openioc','cybox'],
                        help='Genera un IOC en formato especificado.')
    parser.add_argument('-a', '--all-conn', action='store_true',
                        help='Muestra todas las conexiones')
    parser.add_argument('-l', '--live-capture',
                        help='Captura el trafico de una interfaz de red en tiempo real.')
    parser.add_argument('-i', '--incibe',  action='store_true',
                        help='Comprueba que la IP de origen no esté presente en el servicio AntiBotnet de INCIBE.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0.4', help='Muestra la version del programa')
    args = parser.parse_args()

    print('>>> Comprobando integridad del sistema <<<')

    bl_manager = BlackLists()
    bl_manager.carga_listas()

    cmgr = ConexManager()
    procs = Procesos(bl_manager)

    limpios = 0
    maliciosos = 0

    if args.live_capture:
        print('[+] Capturando trafico en %s. Pulsa Ctrl+C para vincular las conexiones a sus procesos.' % args.live_capture)
        pcap = PcapCapture(interface=args.live_capture)

        try:
            for paquete in pcap.captura():

                # Extramos la informacion de la resolucion DNS                    
                if paquete.highest_layer == 'DNS':
                    if paquete.dns.flags_opcode.raw_value == '0':
                        if hasattr(paquete.dns, 'qry_name'):
                            print('DNS query: %s' % paquete.dns.qry_name)
                    try:
                        if paquete.dns.flags_response.raw_value == '1':
                            if hasattr(paquete.dns, 'resp_addr'):
                                print('DNS reply: %s[%s]' % (paquete.dns.qry_name, paquete.dns.resp_addr))
                    except:
                        pass

                if paquete.transport_layer in ('UDP','TCP'):

                    protocolo = cmgr.normaliza_protocolo(paquete.transport_layer)
                    try:
                        src_addr = paquete.ip.src
                        src_port = paquete[paquete.transport_layer].srcport
                    except AttributeError:
                        #print(paquete)
                        #print(dir(paquete))
                        pass

                    dst_addr = paquete.ip.dst
                    dst_port = paquete[paquete.transport_layer].dstport

                    conexion = Conexion(src_addr, src_port, dst_addr, dst_port,
                                        protocolo)

                    if paquete.transport_layer == 'TCP':
                        if paquete.tcp.flags_fin.raw_value == '1' or paquete.tcp.flags_reset.raw_value == '1':
                            # La conexion se está cerrando                       
                            print('CLOSE ', conexion)
                            cmgr.del_conx(conexion)

                    if conexion not in cmgr.lista_conexiones():
                        if bl_manager.es_maliciosa(conexion):
                            conexion.marca_como_maliciosa()
                            print(fail('%s' % conexion))
                        else:
                            print(conexion)
                        cmgr.add_conx(conexion)

        except KeyboardInterrupt:
            print('[!] Buscando los procesos propietarios de estas conexiones...')
            print('En las conexiones UDP es muy probable que su proceso no se encuentre')
            pass

        procs.comprueba_procesos()

        for conn in cmgr.lista_conx_maliciosas():
            proc = procs.busca_conexion(conn)
            if proc:
                print(proc)
            else:
                print('Proceso Desconocido:')
            print(fail('%s' % conn))

             # Generamos el IOC en caso necesario
            if proc and args.generate_profile:
                    fichero = 'ioc_%s.xml' % proc.pid

                    if args.generate_profile == 'openioc':
                        genera_ioc([conn.destino.get_ip()], fichero)
                    elif args.generate_profile == 'cybox':
                        cybox = Cybox()
                        cybox.crea_ipv4(conn.destino.get_ip())
                        cybox.guarda_cybox(fichero)

        print('[!] Terminado')
        sys.exit(0)

    else:
        # Busqueda de procesos utilizando psutil        
        procs.comprueba_procesos()

        for proc in procs.lista_procesos():
            if proc.es_malicioso():
                maliciosos += 1
            else:
                limpios += 1

            if bool(args.show_conn):
                if proc.tiene_conexiones():
                    print(proc)
            else:
                print(proc)

            if args.all_conn:
                # Mostramos todas las conexiones
                for conn in proc.cmgr.lista_conexiones():
                    # Puertos a la escucha
                    if conn.estado is 'LISTEN':
                        print('    * %s' % bold('%s:%s [LISTEN]' % (conn.origen.get_ip(),
                                                                   conn.origen.get_puerto())))

                for conn in proc.cmgr.lista_conx_limpias():
                    # Conexiones establecidas
                    if conn.estado is 'ESTABLISHED':
                        print('    |_ %s' % ok('%s:%s => %s:%s' % (conn.origen.get_ip(),
                                               conn.origen.get_puerto(), conn.destino.get_ip(),
                                               conn.destino.get_puerto())))

            # Mostramos las conexiones maliciosas
            for conn in proc.cmgr.lista_conx_maliciosas():
                print('    |_ %s' % fail('%s:%s => %s:%s' % (conn.origen.get_ip(),
                                    conn.origen.get_puerto(), conn.destino.get_ip(),
                                    conn.destino.get_puerto())))
                if args.generate_profile:
                    fichero = 'ioc_%s.xml' % proc.pid

                    if args.generate_profile == 'openioc':
                        genera_ioc([conn.destino.get_ip()], fichero)
                    elif args.generate_profile == 'cybox':
                        cybox = Cybox()
                        cybox.crea_ipv4(conn.destino.get_ip())
                        cybox.guarda_cybox(fichero)

        print('[+] Procesos: %s LIMPIOS, %s MALICIOSOS' % (ok(limpios), fail(maliciosos)))

    if args.incibe:
        # Comprobamos nuestra IP en el servicio AntiBotNet de INCIBE
        incibe = IncibeAntibotNet()
        incibe.Comprueba()
