# -*- coding: utf-8 -*-


import sys


PY33 = sys.version_info[0:2] >= (3, 3)


template = u"u'{}'"
UnicodeType = unicode
XRangeType = xrange

if PY33:
    template = "'{}'"
    UnicodeType= str
    XRangeType = range
