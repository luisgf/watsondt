#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""

from enum import Enum


class Estado(Enum):
    """ Estado de una Conexion """

    LIMPIA = 1
    MALICIOSA = 2


class Protocolo(Enum):
    """ Protocolo empleado por una conexion """

    TCP = 'TCP'
    UDP = 'UDP'


class ConexManager():
    """ Gestor de Conexiones """

    def __init__(self):
        self._todas = []

    def add_conx(self, conexion):
        """ Añade una conexion a la lista """

        self._todas.append(conexion)

    def del_conx(self, conexion):
        """ Elimina una conexion de la lista """

        if conexion in self._todas:
            self._todas.remove(conexion)

    def lista_conexiones(self):
        """ Devuelve una lista con todas las conexiones """

        return self._todas

    def lista_conx_maliciosas(self):
        """ Devuelve una lista con las conexiones marcadas como maliciosas """

        return [x for x in self._todas if x.estado is Estado.MALICIOSA]

    def lista_conx_limpias(self):
        """ Devuelve una lista con las conexiones marcadas como maliciosas """

        return [x for x in self._todas if x.estado is not Estado.MALICIOSA]

    def en_lista(self, ip):
        """ Devuelve True si la direccion IP se encuentra en la lista """

        if ip in self._todas:
            return True
        else:
            return False

    def normaliza_protocolo(self, protocolo):
        """ Devuelve el tipo de protocolo normalizado """

        if protocolo.lower() == 'udp':
            return Protocolo.UDP
        elif protocolo.lower() == 'tcp':
            return Protocolo.TCP

    def conx_ya_analizada(self, conexion):
        """ Devuelve True si esta conexion origen:puerto => destino:puerto
        ya ha sido analizada """

        for conn in self._todas:
            if conn == conexion:
                return True

        return False

class Conexion():
    """ Gestion de enlaces """

    def __init__(self, src_ip=None, src_port=None, dst_ip=None,
                 dst_port='', proto=None, estado=Estado.LIMPIA):

        self.origen = Socket(src_ip, src_port)
        self.destino = Socket(dst_ip, dst_port)
        self.proto = proto
        self.estado = estado

    def marca_como_maliciosa(self):
        """ Marca la conexion como maliciosa """

        self.estado = Estado.MALICIOSA

    def es_maliciosa(self):
        """ Devuelve True si esta marcada como maliciosa, False
        en caso contrario """

        if self.estado is Estado.MALICIOSA:
            return True
        else:
            return False

    def __str__(self):
        return ('%s => %s %s' % (self.origen, self.destino, self.proto.name))

    def __eq__(self, other):
        """ Sobreescribimos el operador == para poder comparar conexiones """

        return self.origen == other.origen and self.destino == other.destino and self.proto == other.proto

class Socket():
    """ Gestion de sockets """

    def __init__(self, ip, puerto):
        self._ip = ip
        if isinstance(puerto, int):
            self._puerto = puerto
        elif puerto is '*':
            self._puerto = '*'
        else:
            self._puerto = int(puerto, base=10)

    def get_ip(self):
        return self._ip

    def get_puerto(self):
        return self._puerto

    def __str__(self):
        return('%s(%s)' % (self._ip, self._puerto))

    def __eq__(self, other):
        return self.get_ip() == other.get_ip() and self.get_puerto() == other.get_puerto()
