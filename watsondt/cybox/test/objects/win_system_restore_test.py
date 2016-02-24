# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_system_restore_object import WinSystemRestore

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinSystemRestore(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsSystemRestoreObjectType"
    klass = WinSystemRestore

    _full_dict = {
        'restore_point_description': "restore desc",
        'restore_point_full_path': "restore path",
        'acl_change_username': "username",
        'restore_point_name': "pont name",
        'restore_point_type': "point type",
        'backup_file_name': "backup name",
        'acl_change_sid': "an SID",
        'changelog_entry_flags': "entry flags",
        'changelog_entry_sequence_number': 1234,
        #'created' = cybox.TypedField("Created", DateTime)
        'file_attributes': "RWX",
        'new_file_name': "New name",
        'original_file_name': "original file name",
        'original_short_file_name': "org fname",
        'process_name': "A process name",
        'change_event': "some event",
        'changelog_entry_type': "entry type",
        'registry_hive_list': [
            "hive 1",
            "hive 2"
        ],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
