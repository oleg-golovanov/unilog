# -*- coding: utf-8 -*-


import datetime
import unittest

import unilog.convert


class UniTest(unittest.TestCase):

    def test_iterable(self):
        self.assertEqual(
            unilog.as_unicode(
                [
                    datetime.date(2016, 12, 6),
                    datetime.datetime(2016, 12, 6, 11, 22, 33, 444444),
                    'item1',
                    'пункт2',
                    u'пункт3',
                    4,
                    4.44,
                    bytearray([0, 1, 2]),
                    None,
                    True,
                    False
                ]
            ),
            u"[u'2016-12-06', u'2016-12-06 11:22:33.444444', 'item1', 'пункт2', "
            u"u'пункт3', 4, 4.44, b'\\\\x00\\\\x01\\\\x02', None, True, False]"
        )

    def test_mapping(self):
        self.assertEqual(
            unilog.as_str(
                {
                    'generator': (i for i in xrange(3, 6))
                },
                pretty=True
            ),
            "{\n"
            "    'generator': (\n"
            "        3, \n"
            "        4, \n"
            "        5\n"
            "    )\n"
            "}"
        )

    def test_iterable_exception(self):
        self.assertRaises(
            TypeError,
            unilog.convert.uniiterable,
            None, None
        )

    def test_mapping_exception(self):
        self.assertRaises(
            TypeError,
            unilog.convert.unimapping,
            None, None
        )
