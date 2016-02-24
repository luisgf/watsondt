# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.memory_object import Memory
from cybox.test.common.hash_test import EMPTY_MD5
from cybox.test.objects import ObjectTestCase


class TestMemory(ObjectTestCase, unittest.TestCase):
    object_type = "MemoryObjectType"
    klass = Memory

    _full_dict = {
        'custom_properties': [
            {'name': "Prop1", 'description': "Property1", 'value': "Value1"},
            {'name': "Prop2", 'description': "Property2", 'value': "Value2"},
        ],
        'is_injected': True,
        'is_mapped': False,
        'is_protected': True,
        'is_volatile': False,
        'hashes': [{'type': "MD5", 'simple_hash_value': EMPTY_MD5}],
        'name': "A memory region",
        'region_size': 65536,
        'memory_source': ".data",
        'block_type': "Free",
        'region_start_address': "00040000",
        'region_end_address': "00048000",
        'extracted_features': {'functions': ["StringA", "StringB"]},
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
