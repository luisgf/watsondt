# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Hash, String
from cybox.objects.archive_file_object import ArchiveFile
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase

class TestArchiveFile(ObjectTestCase, unittest.TestCase):
    object_type = "ArchiveFileObjectType"
    klass = ArchiveFile

    _full_dict = {
        'archive_format': "ZIP",
        'version': "v2",
        'file_count': 10000,
        'encryption_algorithm': "some algorithm",
        'decryption_key': "abc123key",
        'comment': "This is a test",
        #'archived_file': [],
        
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
