# -*- coding: utf-8 -*-


import sys


PY3 = sys.version_info.major >= 3


if PY3:
    template = "'{}'"
    UnicodeType = str
    XRangeType = range
else:
    template = u"u'{}'"
    UnicodeType = unicode
    XRangeType = xrange
