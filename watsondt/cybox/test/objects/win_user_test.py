# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_user_object import WinUser
from cybox.test.objects import ObjectTestCase


class TestWinUser(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsUserAccountObjectType"
    klass = WinUser

    _full_dict = {
        # Account-specific fields
        'disabled': False,
        'domain': 'ADMIN',
        # UserAccount-specific fields
        'password_required': True,
        'full_name': "Steve Ballmer",
        'group_list': [{'name': "LocalAdministrators"}],
        'home_directory': "C:\\Users\\ballmer\\",
        'last_login': "2011-05-12T07:14:01+07:00",
        'privilege_list': [
                {'user_right': "SeDebugPrivilege"}
            ],
        'username': "ballmer",
        'user_password_age': "P180D",
        # WinUser-specific fields
        'security_id': "S-1-5-21-3623811015-3361044348-30300820-1013",
        'security_type': "SidTypeUser",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
