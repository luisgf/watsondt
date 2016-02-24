# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_computer_account_object import WinComputerAccount
from cybox.test.objects import ObjectTestCase


class TestWinCriticalSection(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsComputerAccountObjectType"
    klass = WinComputerAccount

    _full_dict = {
        'security_id': "An ID",
        'type': "A type",
        'fully_qualified_name': {
            'netbeui_name': "A NetBEUI name",
            'full_name': "A full name"
        },
        'kerberos': {
            'ticket': 9000,
            'delegation': {
                'bitmask': "dead1234",
                'service': {
                    'computer': "Computer goes here",
                    'name': "name goes here",
                    'user': "username here",
                    'port': {
                        'port_value': 80,
                        'layer4_protocol': 'TCP',
                        'xsi:type': "PortObjectType"
                    }
                }
            }
        },
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
