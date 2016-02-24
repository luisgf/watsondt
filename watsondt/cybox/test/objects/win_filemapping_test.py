# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_filemapping_object import WinFilemapping
from cybox.test.objects import ObjectTestCase


class TestWinFilemapping(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsFilemappingObjectType"
    klass = WinFilemapping

    _full_dict = {
        'handle': {
            'id': 1234,
            'name': "MyHandle",
            'type': "Window",
            'object_address': 0xdeadbeef,
            'access_mask': 0x70000000,
            'pointer_count': 3,
            'xsi:type': "WindowsHandleObjectType",
        },
        'file_handle': {
            'id': 5678,
            'name': "MyHandle2",
            'type': "Window",
            'object_address': 0xbeadbeef,
            'access_mask': 0x90009000,
            'pointer_count': 9,
            'xsi:type': "WindowsHandleObjectType",
        },
        'security_attributes': "Attributes go here",
        'name': "A mapping name",
        'maximum_size': 1000,
        'actual_size': 250,
        'page_protection_value': "a protection value",
        'page_protection_attribute': [
            "a protection attribute",
            "another attribute"
        ],
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
