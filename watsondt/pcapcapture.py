#!/usr/bin/env python3
"""

    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""
import sys

try:
    import pyshark
except ImportError:
    print('Dependencia PyShark no instalada!')
    sys.exit(-1)

class PcapCapture():
    """ Captura en tiempo real en formato pcap """

    def __init__(self, interface=None, live_capture=True, pcap_file=None):
        self.interface = interface
        self.live_capture = live_capture
        self.pcap_file = pcap_file

    def captura(self):
        if self.live_capture:
            capture = pyshark.LiveCapture(self.interface)
            return capture.sniff_continuously()

if __name__ == '__main__':
    pcap = PcapCapture(interface='eth0')
    pcap.captura()
