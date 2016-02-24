# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.network_socket_object import NetworkSocket, SocketOptions
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestSocketOptions(EntityTestCase, unittest.TestCase):
    klass = SocketOptions

    _full_dict = {
        'ip_multicast_if': "eth1",  # Should probably be a boolean
        'ip_multicast_if2': "wlan0",  # Should probably be a boolean
        'ip_multicast_loop': False,
        'ip_tos': "true",  # Should probably be a boolean
        'so_broadcast': False,
        'so_conditional_accept': True,
        'so_keepalive': False,
        'so_dontroute': True,
        'so_linger': 17,  # Should probably be a boolean
        'so_dontlinger': True,
        'so_oobinline': False,
        'so_rcvbuf': 44,  # Should probably be a boolean
        'so_group_priority': 19,
        'so_reuseaddr': True,
        'so_debug': False,
        'so_rcvtimeo': 42,  # Should this allow both seconds and microseconds?
        'so_sndbuf': 1000,
        'so_sndtimeo': 22,  # Should this allow both seconds and microseconds?
        'so_update_accept_context': 3,  # Should probably be a boolean
        'so_timeout': 99,
        'tcp_nodelay': False,
    }


class TestNetworkSocket(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkSocketObjectType"
    klass = NetworkSocket

    _full_dict = {
        'is_blocking': False,
        'is_listening': True,
        'address_family': "AF_INET",
        'domain': "PF_INET",
        'local_address': {
            'ip_address': {
                'address_value': "192.168.1.4",
                'xsi:type': "AddressObjectType",
            },
            'xsi:type': "SocketAddressObjectType",
        },
        'options': {'so_broadcast': False},
        'protocol': "IPPROTO_TCP",
        'remote_address': {
            'ip_address': {
                'address_value': "192.168.100.55",
                'xsi:type': "AddressObjectType",
            },
            'port': {
                'port_value': 80,
                'xsi:type': "PortObjectType",
            },
            'xsi:type': "SocketAddressObjectType",
        },
        'type': "SOCK_STREAM",
        'socket_descriptor': 567,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
