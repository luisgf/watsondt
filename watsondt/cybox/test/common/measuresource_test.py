# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import MeasureSource
from cybox.test import EntityTestCase


class TestMeasureSource(EntityTestCase, unittest.TestCase):
    klass = MeasureSource

    _full_dict = {
        'class': "Software",
        'source_type': "Information Source",
        'name': "ASource",
        'information_source_type': "Web Logs",
        'tool_type': "Vulnerability Scanner",
        'description': "A description of the source",
        'contributors': [
            {
                'name': "An amazing dude",
                'email': "amazing@dude.com",
            },
            {
                'name': "Another amazing dude",
                'role': "President of Amazing",
                'organization': "AmazingCo.",
            },
        ],
        'time': {
            'start_time': "2013-02-14T11:28:42-05:00",
            'end_time': "2014-03-11T06:22:17-05:00",
        },
        'tools': [
            {'name': "AmazingTool (TM)"}
        ],
        'platform': {'description': "The best platform"},
        #TODO: Add System and Instance
    }


if __name__ == "__main__":
    unittest.main()
