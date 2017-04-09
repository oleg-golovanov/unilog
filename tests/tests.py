# -*- coding: utf-8 -*-


import datetime
import unittest

import unilog.convert
import unilog.compat


class TestClass(object):

    def __init__(self):
        self.test1 = 'test1'
        self.test2 = 2


class UniTest(unittest.TestCase):

    def test_iterable(self):
        values = {
            'date': u"u'2016-12-06'",
            'datetime': u"u'2016-12-06 11:22:33.444444'",
            'unicode': u"u'пункт3'"
        }
        if unilog.compat.PY3:
            values = {k: v.replace('u', '') for k, v in values.items()}

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
            u"[{date}, {datetime}, 'item1', 'пункт2', {unicode}, 4, 4.44, "
            u"b'\\x00\\x01\\x02', None, True, False]".format(**values)
        )

    def test_mapping(self):
        generator = (i for i in unilog.compat.XRangeType(10))
        result = (
            "{{\n"
            "    'generators': [\n"
            "        '{!r}',\n"
            "        '{}'\n"
            "    ]\n"
            "}}".format(
                generator, 'range(0, 10)' if unilog.compat.PY3 else 'xrange(10)'
            )
        )
        if unilog.compat.PY3:
            result = result.encode(unilog.convert.LOCALE)

        self.assertEqual(
            unilog.as_str(
                {
                    'generators': [
                        generator,
                        unilog.compat.XRangeType(10)
                    ]
                },
                pretty=True
            ),
            result
        )

    def test_register_converter(self):
        unilog.register_converter(
            TestClass,
            lambda x: [x.test1, x.test2]
        )

        self.assertEqual(
            unilog.as_unicode(TestClass()),
            u"['test1', 2]"
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
