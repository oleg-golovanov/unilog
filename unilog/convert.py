# -*- coding: utf-8 -*-


import collections
import locale


LOCALE = locale.getpreferredencoding()

def pretty_spaces (level):
    """
    Return spaces and new line.

    :param level: Deep level
    :return: string with new line and spaces
    """
    if level is None:
        return u''
    return u'{}{}'.format (u'\n' if level > 0 else u'', u''.ljust(4 * level))


def unimapping(arg, level):
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
        result.append(pretty_spaces (level) + u': '.join(map(convert, i, [level] * len(i))))

    return u'{{{}{}}}'.format(u', '.join(result), u'\n' if level else u'')


def uniiterable(arg, level):
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

    if level is None:
        spaces = u''
    else:
        spaces = pretty_spaces (level - 1)
    templates = {
        list: u'{1}[{0}{1}]'.format(u'{}', spaces),
        tuple: u'{1}({0}{1})'.format(u'{}', spaces),
    }

    result = []
    spaces = pretty_spaces (level)
    for i in arg:
        result.append(u''.join((spaces, convert(i, level))))

    return templates.get(type(arg), templates[tuple]).format(u', '.join(result))


def convert(obj, level=None, encoding=LOCALE):
    """
    Covert any object to unicode string.

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)

    :rtype: unicode
    :return: any object as unicode string
    """

    func = lambda x, level: u"u'{}'".format(x)

    if isinstance(obj, unicode):
        # skip if condition, because unicode is a iterable type
        pass
    elif isinstance(obj, str):
        func = lambda x, level: u"'{}'".format(x.decode(encoding))
    elif isinstance(obj, bytearray):
        # double escape to working ast.literal_eval
        func = lambda x, level: u"b'{}'".format(str(x).encode('string-escape').encode('string-escape'))
    elif isinstance(obj, (type(None), int, float)):
        func = lambda x, level: unicode(x)
    elif isinstance(obj, collections.Mapping):
        func = unimapping
    elif isinstance(obj, collections.Iterable):
        func = uniiterable

    if level is None:
        return func (obj, None)
    else:
        return func(obj, level + 1)
