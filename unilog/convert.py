# -*- coding: utf-8 -*-


import os
import types
import locale
import functools
import collections

from . import compat


LOCALE = locale.getpreferredencoding()
INDENT = 4


CONVERTERS = {}


def pretty_spaces(level):
    """
    Return spaces and new line.

    :type level: int or None
    :param level: deep level

    :rtype: unicode
    :return: string with new line and spaces
    """

    if level is None:
        return u''
    return (os.linesep if level >= 0 else u'') + (u' ' * (INDENT * level))


def join_strings(strings, level):
    """
    Define join symbol by level and join strings.
    
    :type strings: collections.Iterable[unicode or str]
    :param strings: strings to join
    :type level: int
    :param level: deep level
    
    :rtype: unicode
    :return: joined string
    """

    return (u', ' if level is None else u',').join(strings)


def unimapping(arg, level):
    """
    Mapping object to unicode string.

    :type arg: collections.Mapping
    :param arg: mapping object
    :type level: int
    :param level: deep level

    :rtype: unicode
    :return: mapping object as unicode string
    """

    if not isinstance(arg, collections.Mapping):
        raise TypeError(
            'expected collections.Mapping, {} received'.format(type(arg).__name__)
        )

    result = []
    for i in arg.items():
        result.append(
            pretty_spaces(level) + u': '.join(map(functools.partial(convert, level=level), i))
        )

    string = join_strings(result, level)
    if level is not None:
        string += pretty_spaces(level - 1)

    return u'{{{}}}'.format(string)


def uniiterable(arg, level):
    """
    Iterable object to unicode string.

    :type arg: collections.Iterable
    :param arg: iterable object
    :type level: int
    :param level: deep level

    :rtype: unicode
    :return: iterable object as unicode string
    """

    if not isinstance(arg, collections.Iterable):
        raise TypeError(
            'expected collections.Iterable, {} received'.format(type(arg).__name__)
        )

    templates = {
        list: u'[{}]',
        tuple: u'({})'
    }

    result = []
    for i in arg:
        result.append(pretty_spaces(level) + convert(i, level=level))

    string = join_strings(result, level)
    if level is not None:
        string += pretty_spaces(level - 1)

    return templates.get(type(arg), templates[tuple]).format(string)


def convert(obj, encoding=LOCALE, level=None):
    """
    Covert any object to unicode string.

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)
    :type level: int
    :param level: Deep level. If None level is not considered.

    :rtype: unicode
    :return: any object as unicode string
    """

    callable_ = CONVERTERS.get(type(obj))
    if callable_ is not None:
        obj = callable_(obj)

    func = lambda x, level: compat.template.format(x)

    if isinstance(obj, compat.UnicodeType):
        # skip if condition, because unicode is a iterable type
        pass
    elif isinstance(obj, str):
        func = lambda x, level: u"'{}'".format(x.decode(encoding))
    elif isinstance(obj, (bytearray, bytes)):
        func = lambda x, level: u"b'{}'".format(
            u''.join(u'\\x{:02x}'.format(b) for b in x)
        )
    elif isinstance(obj, (type(None), int, float)):
        func = lambda x, level: compat.UnicodeType(x)
    elif isinstance(obj, (types.GeneratorType, compat.XRangeType)):
        func = lambda x, level: u"'{!r}'".format(x)
    elif isinstance(obj, collections.Mapping):
        func = unimapping
    elif isinstance(obj, collections.Iterable):
        func = uniiterable

    if level is not None:
        level += 1

    return func(obj, level)
