# -*- coding: utf-8 -*-


import collections
import locale


LOCALE = locale.getpreferredencoding()


def unimapping(arg):
    """
    Mapping object to unicode string.

    :type arg: collections.Mapping
    :param arg: mapping object

    :rtype: unicode
    :return: mapping object as unicode string
    """

    if not isinstance(arg, collections.Mapping):
        raise TypeError(
            'expected collections.Mapping, {} received'.format(type(arg).__name__)
        )

    result = []
    for k, v in arg.items():
        k = convert(k)

        result.append(u'{}: {}'.format(
            k,
            convert(v))
        )

    return u'{{{}}}'.format(u', '.join(result))


def uniiterable(arg):
    """
    Iterable object to unicode string.

    :type arg: collections.Iterable
    :param arg: iterable object

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
        result.append(convert(i))

    return templates.get(type(arg), templates[tuple]).format(u', '.join(result))


def convert(obj, encoding=LOCALE):
    """
    Covert any object to unicode string.

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)

    :rtype: unicode
    :return: any object as unicode string
    """

    if isinstance(obj, unicode):
        func = lambda x: u"u'{}'".format(x)
    elif isinstance(obj, str):
        func = lambda x: u"'{}'".format(x.decode(encoding))
    elif isinstance(obj, (int, float)):
        func = lambda x: unicode(x)
    elif isinstance(obj, collections.Mapping):
        func = unimapping
    elif isinstance(obj, collections.Iterable):
        func = uniiterable
    else:
        func = lambda x: x

    return func(obj)
