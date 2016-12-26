# -*- coding: utf-8 -*-


import convert


def as_unicode(obj, pretty=False, encoding=convert.LOCALE):
    """
    Representing any object to unicode string.

    :param obj: any object
    :type pretty: bool
    :param pretty: Pretty print.
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)

    :rtype: unicode
    :return: any object as unicode string
    """

    return convert.convert(obj, 0 if pretty else None, encoding)


def as_str(obj, pretty=False, encoding=convert.LOCALE):
    """
    Representing any object to string.

    :param obj: any object
    :type pretty: bool
    :param pretty: Pretty print.
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)

    :rtype: str
    :return: any object as string
    """

    return as_unicode(obj, pretty, encoding).encode(encoding)
