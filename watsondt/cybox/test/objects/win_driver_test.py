# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_driver_object import WinDriver

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinDriver(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsDriverObjectType"
    klass = WinDriver

    _full_dict = {
        'driver_init': 123,
        'driver_name': "A driver name",
        'driver_object_address': "abcde12345",
        'driver_start_io': "abcce4321",
        'driver_unload': "ab3234dec",
        'image_base': "12345abc",
        'image_size': "12ff",
        'irp_mj_cleanup': 1,
        'irp_mj_close': 2,
        'irp_mj_create': 3,
        'irp_mj_create_mailslot': 4,
        'irp_mj_create_named_pipe': 5,
        'irp_mj_device_change': 6,
        'irp_mj_device_control': 7,
        'irp_mj_directory_control': 8,
        'irp_mj_file_system_control': 9,
        'irp_mj_flush_buffers': 11,
        'irp_mj_internal_device_control': 12,
        'irp_mj_lock_control': 13,
        'irp_mj_pnp': 14,
        'irp_mj_power': 15,
        'irp_mj_query_ea': 16,
        'irp_mj_query_information': 17,
        'irp_mj_query_quota': 22,
        'irp_mj_query_security': 23,
        'irp_mj_query_volume_information': 24,
        'irp_mj_read': 25,
        'irp_mj_set_ea': 26,
        'irp_mj_set_information': 27,
        'irp_mj_set_quota': 33,
        'irp_mj_set_security': 34,
        'irp_mj_set_volume_information': 35,
        'irp_mj_shutdown': 36,
        'irp_mj_system_control': 37,
        'irp_mj_write': 38,   
        #'device_object_list' = TypedField("Device_Object_List", DeviceObjectList)
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
