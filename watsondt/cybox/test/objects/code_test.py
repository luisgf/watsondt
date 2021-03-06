# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.code_object import Code
from cybox.test.objects import ObjectTestCase


class TestCode(ObjectTestCase, unittest.TestCase):
    object_type = "CodeObjectType"
    klass = Code

    _full_dict = {
        #TODO: add other fields
        'description': "Some code",
        'type': "Foo",
        'purpose': "Demonstration",
        'code_language': "C++",
        'start_address': "00040000",
        'code_segment': "int a = 1",
        'code_segment_xor': {
            'value': "1234",
            'condition': "Equals",
            # TODO: add xor_pattern
            #'xor_pattern': "01020304"
        },
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
