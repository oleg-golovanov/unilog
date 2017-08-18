# -*- coding: utf-8 -*-


from . import convert


def as_unicode(obj, encoding=convert.LOCALE, pretty=False):
    """
    Representing any object to <unicode> string (python2.7) or <str> string (python3.0).

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)
    :type pretty: bool
    :param pretty: pretty print

    :rtype: unicode
    :return: any object as unicode string
    """

    return convert.convert(obj, encoding, 0 if pretty else None)


def as_str(obj, encoding=convert.LOCALE, pretty=False):
    """
    Representing any object to <str> string (python2.7) or <bytes> string (python3.0).

    :param obj: any object
    :type encoding: str
    :param encoding: codec for encoding unicode strings
                     (locale.getpreferredencoding() by default)
    :type pretty: bool
    :param pretty: pretty print

    :rtype: str
    :return: any object as string
    """

    return as_unicode(obj, encoding, pretty).encode(encoding)


def register_converter(typename, callable_):
    """
    Registers a callable to convert typename instance.

    :param typename: any class
    :param callable_: any callable object
    """

    convert.CONVERTERS[typename] = callable_
