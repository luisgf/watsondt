# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_registry_key_object import WinRegistryKey
from cybox.test.objects import ObjectTestCase


class TestWinRegistryKey(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsRegistryKeyObjectType"
    klass = WinRegistryKey

    _full_dict = {
        'key': "\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting",
        'hive': "HKEY_LOCAL_MACHINE",
        'number_values': 6,
        'values': [
            {
                'name': "Disabled",
                'data': "1",
                'datatype': "REG_DWORD",
                'byte_runs': [{'length': 1, 'byte_run_data': "A"}],
            },
            {
                'name': "ErrorPort",
                'data': "\\WindowsErrorReportingServicePort",
                'datatype': "REG_SZ",
            },
        ],
        'modified_time': "2013-08-08T15:15:15-04:00",
        'creator_username': "gback",
        'handle_list': [
            {
                'name': "RegHandle",
                'pointer_count': 1,
                'type': "RegistryKey",
                'xsi:type': 'WindowsHandleObjectType',
            },
        ],
        'number_subkeys': 1,
        'subkeys': [
            {
                'key': "Consent",
                'number_values': 1,
                'values': [
                    {
                        'name': "NewUserDefaultConsent",
                        'data': "1",
                        'datatype': "REG_DWORD",
                    },
                ],
                'xsi:type': 'WindowsRegistryKeyObjectType',
            },
        ],
        'byte_runs': [
            {'length': 4, 'byte_run_data': "z!%f"},
            {'offset': 0x1000, 'length': 8, 'byte_run_data': "%40V.,2@"},
        ],
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
