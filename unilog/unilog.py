# -*- coding: utf-8 -*-


import convert


def as_unicode(obj, encoding=convert.LOCALE, pretty=False):
    """
    Representing any object to unicode string.

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)
    :type pretty: bool
    :param pretty: Pretty print.

    :rtype: unicode
    :return: any object as unicode string
    """

    return convert.convert(obj, encoding, 0 if pretty else None)


def as_str(obj, encoding=convert.LOCALE, pretty=False):
    """
    Representing any object to string.

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)
    :type pretty: bool
    :param pretty: Pretty print.

    :rtype: str
    :return: any object as string
    """

    return as_unicode(obj, encoding, pretty).encode(encoding)
