#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""

import sys
from socket import SOCK_STREAM
from enum import Enum

try:
    from psutil import process_iter, NoSuchProcess, AccessDenied
except ImportError:
    print('[!] Libreria psutil no instalada. Porfavor, instala la dependencia')
    sys.exit(-1)

from conexiones import ConexManager, Conexion, Protocolo, Estado
from colores import fail

class Proceso():
    """ Gestion de Procesos del Sistema """

    def __init__(self, pid=None, nombre=None, imagen=None, conexiones=None):
        self.pid = pid
        self.nombre = nombre
        self.imagen = imagen
        self.cmgr = ConexManager() # Gestor de Conexiones        

        """ Extraccion de Conexiones del sistema """
        self._conexiones(conexiones)

    def __str__(self):
        msg = '[!] Proceso{%s(%s)} %s' % (self.nombre, self.pid, self.imagen)
        if self.es_malicioso():
            return fail(msg)
        else:
            return msg

    def _conexiones(self, conexiones):
        """ Procesa las conexiones establecidas por los procesos """
        if conexiones:
            for conn in conexiones:
                if conn.type == SOCK_STREAM:
                    proto = Protocolo.TCP
                else:
                    proto = Protocolo.UDP

                src_ip, src_port = conn.laddr[0], conn.laddr[1]

                if conn.raddr:
                    dst_ip, dst_port = conn.raddr[0], conn.raddr[1]
                else:
                    dst_ip, dst_port = '0.0.0.0', '*'

                c = Conexion(src_ip, src_port ,dst_ip, dst_port, proto,
                             conn.status)

                self.cmgr.add_conx(c)

    def es_malicioso(self):
        """ Devuelve True si el proceso gestiona una conexion marcada
            como maliciosa """

        if len(self.cmgr.lista_conx_maliciosas()) > 0:
            return True
        else:
            return False

    def tiene_conexiones(self):
        """ Devuelve True si hay alguna conexion, sino False """

        if len(self.cmgr.lista_conexiones()) > 0:
            return True
        else:
            return False

class Procesos():
    """ Gestion de procesos del Sistema Operativo """

    def __init__(self, bl_manager=None):
        self.blm = bl_manager  # BlackList Manager
        self.proclist = list()  # Lista de procesos

    def lista_procesos(self):
        """ Adquiere la lista de procesos en ejecucion del OS """
        for item in process_iter():
            try:
                data = item.as_dict(attrs=['pid', 'name', 'connections'])
                self.proclist.append(Proceso(pid=data['pid'],
                                             nombre=data['name'], imagen=item.exe(),
                                             conexiones=data['connections']))

            except AccessDenied:
                print('[!] Problema de acceso!! Ejecuta ese programa como root/Adminsitrador')
                sys.exit(-1)
            except PermissionError:
                print('[!] Problema de acceso!! Ejecuta ese programa como root/Adminsitrador')
                sys.exit(-1)
        return self.proclist

    def comprueba_procesos(self):
        """ Comprueba las conexiones activas que mantienen los procesos """

        for proc in self.lista_procesos():
            for conn in proc.cmgr.lista_conexiones():
                if self.blm.es_maliciosa(conn):
                    conn.marca_como_maliciosa()

    def busca_conexion(self, conexion):
        """ Devuelve el proceso que gestiona una determinada conexion """

        for proc in self.lista_procesos():
            for conn in proc.cmgr.lista_conexiones():
                if conn == conexion:
                    return proc
        return False

if __name__ == '__main__':
    pass
