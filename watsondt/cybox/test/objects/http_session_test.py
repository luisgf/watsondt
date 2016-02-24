# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.address_object import Address
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.uri_object import URI
from cybox.test.objects import ObjectTestCase


class TestHTTPSession(ObjectTestCase, unittest.TestCase):
    object_type = "HTTPSessionObjectType"
    klass = HTTPSession

    _full_dict = {
        'http_request_response': [
            {
                'http_client_request': {
                    'http_request_line': {
                        'http_method': "GET",
                        'value': "/index.html",
                        'version': "http/1.1",
                    },
                    'http_request_header': {
                        'raw_header': "...ALL THE REQUEST HEADERS...",
                        'parsed_header': {
                            'accept': "text/plain",
                            'accept_charset': "utf-8",
                            'accept_language': "en-US",
                            'accept_datetime':
                                    "Thu, 31 May 2007 20:35:00 GMT",
                            'accept_encoding': "gzip, deflate",
                            'authorization': "Basic QWxhZGRbpjpvc",
                            'cache_control': "no-cache",
                            'connection': "keep-alive",
                            'cookie': "$Version=1; Skin=new;",
                            'content_length': 348,
                            'content_md5': "Q2hlY2sgSW50ZWdyaXR5IQ==",
                            'content_type': "application/xml",
                            'date': "1994-11-15T08:12:31+00:00",
                            'expect': "200-ok",
                            'from': {'address_value': "bob@example.com",
                                        'category': Address.CAT_EMAIL,
                                        'xsi:type': "AddressObjectType"},
                            'host': {
                                'domain_name': {
                                    'value': "en.wikipedia.org",
                                    'type': URI.TYPE_DOMAIN,
                                    'xsi:type': "URIObjectType"
                                },
                                'port': {
                                    'port_value': 80,
                                    'layer4_protocol': "TCP",
                                    'xsi:type': "PortObjectType"
                                }
                            },
                            'if_match':
                                    "737060cd8c284d8af7ad3082f209582d",
                            'if_modified_since':
                                    "1994-10-29T19:43:31+00:00",
                            'if_none_match':
                                    "737060cd8c284d8af7ad3082f209582e",
                            'if_range':
                                    "737060cd8c284d8af7ad3082f209582f",
                            'if_unmodified_since':
                                    "1996-11-22T09:33:32+00:00",
                            'max_forwards': 10,
                            'pragma': "no-cache",
                            'proxy_authorization': "Basic QwxhZ==",
                            'range': "bytes=500-999",
                            'referer': {
                                'value': "http://en.wikipedia.org/wiki",
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                            'te': "trailers, deflate",
                            'user_agent': "Mozilla/5.0 Firefox/21.0",
                            'via': "1.0 fred, 1.1 example.com",
                            'warning': "199 Miscellaneous warning",
                            'dnt': "1 (Do Not Track Enabled)",
                            'x_requested_with': "XMLHttpRequest",
                            'x_forwarded_for': "client1, proxy1",
                            'x_forwarded_proto': "https",
                            'x_att_deviceid': "MakeModel/Firmware",
                            'x_wap_profile': {
                                'value': "http://samsung.com/SGHI777.xml",
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                        }
                    },
                    'http_message_body': {
                        'length': 10,
                        'message_body': "Hi there!!",
                    }
                },
            },
            {
                'http_server_response': {
                    'http_status_line': {
                        'version': "http/1.0",
                        'status_code': 200,
                        'reason_phrase': "OK"
                    },
                    'http_response_header': {
                        'raw_header': "...ALL THE RESPONSE HEADERS...",
                        'parsed_header': {
                            'access_control_allow_origin': "*",
                            'accept_ranges': "bytes",
                            'age': 12,
                            'cache_control': "max-age=3600",
                            'connection': "close",
                            'content_encoding': "gzip",
                            'content_language': "da",
                            'content_length': 348,
                            'content_location': "/index.htm",
                            'content_md5': "Q2hlY2sgSW50ZWdyaXR5IQ==",
                            'content_disposition': "attachment; filename",
                            'content_range': "bytes 21010-47021",
                            'content_type': "text/html; charset=utf-8",
                            'date': "1994-11-15T08:12:31+00:00",
                            'etag': '"737060cd8c284d8af7ad3082f20"',
                            'expires': "1994-12-01T16:00:00+00:00",
                            'last_modified': "1994-11-15T16:00:00+00:00",
                            'link': '1</feed>; rel="alternate"',
                            'location': {
                                'value': "http://www.w3c.org/pub/hi.html",
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                            'p3p': "CP=\"This is not a P3P policy!\"",
                            'pragma': "no-cache",
                            'proxy_authenticate': "Basic",
                            'refresh': "5",
                            'retry_after': 120,
                            'server': "Apache/2.4.1 (Unix)",
                            'set_cookie': "UserID=JohnDoe, Version=1",
                            'strict_transport_security': "max-age=160740",
                            'trailer': "Max-Forwards",
                            'transfer_encoding': "chunked",
                            'vary': "*",
                            'via': "1.0 fred, 1.1 example.com",
                            'warning': "199 Miscellaneous warning",
                            'www_authenticate': "Basic",
                            'x_frame_options': "deny",
                            'x_xss_protection': "1; mode=block",
                            'x_content_type_options': "nosniff",
                            'x_powered_by': "PHP/5.4.0",
                            'x_ua_compatible': "Chrome=1",
                        }
                    },
                    'http_message_body': {
                        'length': 26,
                        'message_body': "<html><head></head></html>",
                    }
                },
            },
        ],
        'xsi:type': object_type,
    }

    def test_object_reference(self, ref_dict=None):
        # We have to put at least some content in here, since at least one
        # HTTPRequestResponse is required by the bindings for the round trip.
        sess_dict = {
            'http_request_response': [{
                    'http_client_request': {
                        'http_request_line': {'http_method': "GET"}
                    }
            }]
        }
        ObjectTestCase.test_object_reference(self, sess_dict)


if __name__ == "__main__":
    unittest.main()
