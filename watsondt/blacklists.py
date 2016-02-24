#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""

import os
from netaddr import IPAddress, iter_iprange, cidr_merge

LISTS_PATH = './lists'


class BlackLists():
    """
        Controlador de Listas de reputacion.
    """
    def __init__(self):
        self.block_lists = list()

    def carga_listas(self):
        """ Carga una lista de reputacion desde un fichero """
        for file in os.listdir(LISTS_PATH):
            with open('%s/%s' % (LISTS_PATH, file), 'rb') as fichero:
                data = fichero.readlines()

            if data:
                for lin in data:
                    lin = lin.decode('utf-8').strip('\n\r')
                    if lin and lin[0] != '#':
                        ipentry = lin.split(':')
                        self.block_lists += network_merge(ipentry[1])
        print('[!] %d entradas en la blacklists cargadas' % len(self.block_lists))

    def es_maliciosa(self, conexion):
        """ Esta funcion devuelve True si la ip de origen o destino esta
        listada en alguna de las black lists """

        dir_ip = conexion.origen.get_ip()
        for block in self.block_lists:
            if IPAddress(dir_ip) in block:
                return True

        dir_ip = conexion.destino.get_ip()
        for block in self.block_lists:
            if IPAddress(dir_ip) in block:
                return True

        return False


def network_merge(ipblock):
    """ Agrupamos las direcciones de red """
    dir_ip = ipblock.split('-')
    ip_list = list(iter_iprange(dir_ip[0], dir_ip[1]))
    return cidr_merge(ip_list)


if __name__ == '__main__':
    pass
