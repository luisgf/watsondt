#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""
from io import StringIO
from cybox import helper
from cybox.core import Observables

class Cybox():
    def __init__(self):
        self.helper = None

    def crea_ipv4(self, ip):
        """ Crea un helper para una dirección IP y devuelve un Observable  """

        self.helper = helper.create_ipv4_observable(ip)

    def get_xml(self):
        """ Devuelve un observable en formato XML """

        return Observables([self.helper]).to_xml()

    def guarda_cybox(self, fichero):
        """ Guarda el indicador Cybox XML en disco """

        if self.helper:
            with open(fichero, 'wb') as f:
                f.write(self.get_xml())

        print('[+] Indicador Cybox guardado en: %s' % fichero)
if __name__ == '__main__':
    pass

