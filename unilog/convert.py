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
    for i in arg.items():
        result.append(u': '.join(map(convert, i)))

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

    func = lambda x: u"u'{}'".format(x)

    if isinstance(obj, unicode):
        # skip if condition, because unicode is a iterable type
        pass
    elif isinstance(obj, str):
        func = lambda x: u"'{}'".format(x.decode(encoding))
    elif isinstance(obj, (type(None), int, float)):
        func = lambda x: unicode(x)
    elif isinstance(obj, collections.Mapping):
        func = unimapping
    elif isinstance(obj, collections.Iterable):
        func = uniiterable

    return func(obj)
