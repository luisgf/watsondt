# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Hash, String
from cybox.objects.image_file_object import ImageFile
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase

class TestImageFile(ObjectTestCase, unittest.TestCase):
    object_type = "ImageFileObjectType"
    klass = ImageFile

    _full_dict = {
        'image_is_compressed': True,
        'image_file_format': "JPG",
        'image_height': 10000,
        'image_width': 3000,
        'bits_per_pixel': 9000,
        'compression_algorithm': "An algorithm",
        
        'is_packed': False,
        'is_masqueraded': True,
        'file_name': "example.txt",
        'file_path': {'value': "C:\\Temp",
                      'fully_qualified': True},
        'device_path': "\\Device\\CdRom0",
        'full_path': "C:\\Temp\\example.txt",
        'file_extension': "txt",
        'size_in_bytes': 1024,
        'magic_number': "D0CF11E0",
        'file_format': "ASCII Text",
        'hashes': [
            {
                'type': Hash.TYPE_MD5,
                'simple_hash_value': "0123456789abcdef0123456789abcdef"
            }
        ],
        'digital_signatures': [
            {
                'certificate_issuer': "Microsoft",
                'certificate_subject': "Notepad",
            }
        ],
        'modified_time': "2010-11-06T02:02:02+08:00",
        'accessed_time': "2010-11-07T02:03:02+09:00",
        'created_time': "2010-11-08T02:04:02+10:00",
        'user_owner': "sballmer",
        'packer_list': [
            {
                'name': "UPX",
                'version': "3.91",
            }
        ],
        'peak_entropy': 7.454352453,
        'sym_links': ["../link_destination"],
        'byte_runs': [{'offset': 16, 'byte_run_data': "1A2B3C4D"}],
        'extracted_features': {
            'strings': [{'string_value': "string from the file"}],
        },
        'encryption_algorithm': "RC4",
        'compression_method': "deflate",
        'compression_version': "1.0",
        'compression_comment': "This has been compressed",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
