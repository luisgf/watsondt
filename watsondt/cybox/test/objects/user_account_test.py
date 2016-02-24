# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.user_account_object import UserAccount
from cybox.test.objects import ObjectTestCase


class TestUserAccount(ObjectTestCase, unittest.TestCase):
    object_type = "UserAccountObjectType"
    klass = UserAccount

    _full_dict = {
        # Account-specific fields
        'disabled': False,
        'locked_out': True,
        'description': 'An account',
        'domain': 'ADMIN',
        # UserAccount-specific fields
        # (cannot test group_list of privilege_list since
        # they are abstract)
        'password_required': True,
        'full_name': "Guido van Rossum",
        'home_directory': "/home/guido/",
        'last_login': "2001-01-01T06:56:50+04:00",
        'script_path': "/bin/bash",
        'username': "guido",
        'user_password_age': "P90D",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
