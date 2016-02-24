#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Módulo de detección de BotNets usando el servidio de INCIBE

    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

    apt-get install zlib1g-dev libxslt-dev libxml2 libxml2-dev

"""

import requests
import json

class IncibeAntibotNet():

    def __init__(self, acceso='api'):
        self.acceso = acceso


    def Comprueba(self):
        """ Comprueba que la IP de origen de la peticion no figure en el
            servicio ANTIBOTNET de INCIBE """

        headers = {'X_INTECO_WS_Request_Source':'api', 'User-Agent':'luisgf.es IOC program'}
        try:
            r = requests.get('https://antibotnet.osi.es/api/wscheckip/es/',
                         headers=headers, timeout=5)
        except requests.ConnectionError:
            print('[!] Error HTTP encontrado, consultando el servicio AntiBotNet de INCIBE.')
            return True

        if r.status_code == requests.codes.ok:
            json_res = json.loads(r.text)
            if len(json_res['evidences']) > 0:
                print('[!] La ip %s figura en el servicio antibotnet de INCIBE' % (json_res['ip']))
                return True
            else:
                print('[!] La ip %s NO figura en el servicio antibotnet de INCIBE' % (json_res['ip']))
                return False
        else:
            print('[!] Error HTTP encontrado, consultando el servicio AntiBotNet de INCIBE.')
            return True

if __name__ == '__main__':
   incibe = IncibeAntibotNet()
   incibe.Comprueba()

