# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import ExtractedFeatures
from cybox.test import EntityTestCase

# Need to do this so the binding class is registered.
import cybox.bindings.cybox_common
from cybox.bindings.address_object import AddressObjectType
setattr(cybox.bindings.cybox_common, "AddressObjectType", AddressObjectType)

class TestExtractedFeatures(EntityTestCase, unittest.TestCase):
    klass = ExtractedFeatures

    _full_dict = {
        'strings': [
            {'encoding': "ASCII", 'string_value': "A String", 'length': 8},
            {'encoding': "UTF-8", 'string_value': "Another String"},
        ],
        'imports': ["CreateFileA", "LoadLibrary"],
        'functions': ["DoSomething", "DoSomethingElse"],
        #TODO: Use CodeObject instead of AddressObject
        'code_snippets': [
            {'address_value': "8.8.8.8", 'xsi:type': "AddressObjectType"},
            {'address_value': "1.2.3.4", 'xsi:type': "AddressObjectType"},
        ],
    }


if __name__ == "__main__":
    unittest.main()
