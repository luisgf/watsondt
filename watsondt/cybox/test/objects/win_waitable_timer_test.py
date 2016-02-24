# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_waitable_timer_object import WinWaitableTimer

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinWaitableTimer(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsWaitableTimerObjectType"
    klass = WinWaitableTimer

    _full_dict = {
        'security_attributes': "timer attributes",
        'name': "timer name",
        'type': "timer type",
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
