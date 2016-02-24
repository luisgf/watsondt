# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_task_object import WinTask
from cybox.test.common.hash_test import TEST_HASH_LIST
from cybox.test.objects import ObjectTestCase


class TestWinTask(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsTaskObjectType"
    klass = WinTask

    _full_dict = {
        'status': "SCHED_S_TASK_RUNNING",
        'priority': "NORMAL_PRIORITY_CLASS",
        'name': "Find all the malware",
        'application_name': "Windows Defender",
        'parameters': "C:\\",
        'flags': "/DEEP",
        'account_name': "SYSTEM",
        'account_run_level': "ARunLevel",
        'account_logon_type': "S4U",
        'creator': "TheCreator",
        'creation_date': "2012-04-26T15:30:45-05:00",
        'most_recent_run_time': "2013-06-26T10:20:30-05:00",
        'exit_code': 0,
        'max_run_time': 15000,
        'next_run_time': "2013-06-27T10:20:30-05:00",
        'action_list': [
            {
                'action_type': "TASK_ACTION_SEND_EMAIL",
                'action_id': "Action #1",
                'iemailaction': {
                    'raw_body': "Task Completed!",
                    'xsi:type': "EmailMessageObjectType",
                },
            },
            {
                'action_type': "TASK_ACTION_COM_HANDLER",
                'action_id': "Action #2",
                'icomhandleraction': {
                    'com_data': "COMDATA",
                    'com_class_id': "CLASSID"
                },
            },
            {
                'action_type': "TASK_ACTION_EXEC",
                'action_id': "Action #3",
                'iexecaction': {
                    'exec_arguments': "ARGS",
                    'exec_program_path': "C:\\temp\\cmd.exe",
                    'exec_working_directory': "C:\\temp\\",
                    'exec_program_hashes': TEST_HASH_LIST,
                },
            },
            {
                'action_type': "TASK_ACTION_SHOW_MESSAGE",
                'action_id': "Action #4",
                'ishowmessageaction': {
                    'show_message_body': "Task completed.",
                    'show_message_title': "Task Complete",
                },
            },
        ],
        'trigger_list': [
            {
                'trigger_begin': "2013-05-05T01:02:03-04:00",
                'trigger_delay': "PT5M",
                'trigger_end': "2013-05-05T01:02:10-04:00",
                'trigger_frequency':
                    "TASK_TIME_TRIGGER_DAILY",
                'trigger_max_run_time': "PT1M",
                'trigger_session_change_type':
                    "TASK_REMOTE_CONNECT",
                #TODO: Add trigger_type
            },
            {
                'trigger_max_run_time': "PT10M",
            },
        ],
        'comment': "This is a useless task.",
        'working_directory': "C:\\WINDOWS\\system32\\",
        'work_item_data': "AAAAn34lq21b4m2nbvoi345",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
