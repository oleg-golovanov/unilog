unilog
------

|Version| |PyVersions| |PyImplementations| |Status| |Coverage| |License|

Unilog module aimed at facilitating the development and logging complex data structures, mainly for python2.7.
In python3, there is no such pain when printing complex data structures, so python3 support is due to backward
compatibility with the old code. But for python3, the functionality of registering converters will be useful,
for printing or logging complex data structures that do not override the __str__ method or need to represent them
in a different way. The functionality of registering converters is also available for python2.7.

Unilog provides 3 functions (their description can be obtained by the help function):

* as_unicode
* as_str
* register_converter

Installation
------------
::

    $ pip install unilog

Example
-------
.. code-block:: python

    data = {
        'date': datetime.date(2016, 12, 6),
        'datetime': datetime.datetime(2016, 12, 6, 11, 22, 33, 444444),
        'str': 'item1',
        'str2': 'пункт2',
        u'юникод': u'пункт3',
        'int': 4,
        'float': 4.44,
        'bytearray': bytearray([0, 1, 2]),
        'NoneType': None,
        'True': True,
        'False': False,
        'list': [
            datetime.date(2016, 12, 6), datetime.datetime(2016, 12, 6, 11, 22, 33, 444444),
            'item1', 'пункт2', u'пункт3', 4, 4.44, bytearray([0, 1, 2]), None, True, False
        ],
        'tuple': (
            datetime.date(2016, 12, 6), datetime.datetime(2016, 12, 6, 11, 22, 33, 444444),
            'item1', 'пункт2', u'пункт3', 4, 4.44, bytearray([0, 1, 2]), None, True, False
        ),
        'generator': (i for i in xrange(3, 6))
    }

    # default python2.7 behavior
    >>> print unicode(data)
    {'bytearray': bytearray(b'\x00\x01\x02'), 'tuple': (datetime.date(2016, 12, 6),
    datetime.datetime(2016, 12, 6, 11, 22, 33, 444444), 'item1',
    '\xd0\xbf\xd1\x83\xd0\xbd\xd0\xba\xd1\x822', u'\u043f\u0443\u043d\u043a\u04423', 4, 4.44,
    bytearray(b'\x00\x01\x02'), None, True, False), 'int': 4, 'float': 4.44,
    'datetime': datetime.datetime(2016, 12, 6, 11, 22, 33, 444444), 'date': datetime.date(2016, 12, 6),
    'False': False, 'generator': <generator object <genexpr> at 0x7ff51a58df00>,
    'str2': '\xd0\xbf\xd1\x83\xd0\xbd\xd0\xba\xd1\x822', 'list': [datetime.date(2016, 12, 6),
    datetime.datetime(2016, 12, 6, 11, 22, 33, 444444), 'item1',
    '\xd0\xbf\xd1\x83\xd0\xbd\xd0\xba\xd1\x822', u'\u043f\u0443\u043d\u043a\u04423', 4, 4.44,
    bytearray(b'\x00\x01\x02'), None, True, False], 'str': 'item1',
    u'\u044e\u043d\u0438\u043a\u043e\u0434': u'\u043f\u0443\u043d\u043a\u04423', 'True': True,
    'NoneType': None}

    # use unilog.as_unicode function
    >>> print unilog.as_unicode(data)
    {'bytearray': b'\\x00\\x01\\x02', 'tuple': (u'2016-12-06', u'2016-12-06 11:22:33.444444', 'item1',
    'пункт2', u'пункт3', 4, 4.44, b'\\x00\\x01\\x02', None, True, False), 'int': 4, 'float': 4.44,
    'datetime': u'2016-12-06 11:22:33.444444', 'date': u'2016-12-06', 'False': False,
    'generator': '<generator object <genexpr> at 0x7ff51a58df00>', 'str2': 'пункт2',
     'list': [u'2016-12-06', u'2016-12-06 11:22:33.444444', 'item1', 'пункт2', u'пункт3', 4, 4.44,
     b'\\x00\\x01\\x02', None, True, False], 'str': 'item1', u'юникод': u'пункт3', 'True': True, 'NoneType': None}

    # use unilog.as_unicode function with pretty print
    >>> print unilog.as_unicode(data, pretty=True)
    {
        'bytearray': b'\\x00\\x01\\x02',
        'tuple': (
            u'2016-12-06',
            u'2016-12-06 11:22:33.444444',
            'item1',
            'пункт2',
            u'пункт3',
            4,
            4.44,
            b'\\x00\\x01\\x02',
            None,
            True,
            False
        ),
        'int': 4,
        'float': 4.44,
        'datetime': u'2016-12-06 11:22:33.444444',
        'date': u'2016-12-06',
        'False': False,
        'generator': '<generator object <genexpr> at 0x7ff51a58df00>',
        'str2': 'пункт2',
        'list': [
            u'2016-12-06',
            u'2016-12-06 11:22:33.444444',
            'item1',
            'пункт2',
            u'пункт3',
            4,
            4.44,
            b'\\x00\\x01\\x02',
            None,
            True,
            False
        ],
        'str': 'item1',
        u'юникод': u'пункт3',
        'True': True,
        'NoneType': None
    }

License
-------
MIT licensed. See the bundled `LICENSE <https://github.com/oleg-golovanov/unilog/blob/master/LICENSE>`_ file for more details.

.. |Version| image:: https://img.shields.io/pypi/v/unilog.svg
    :target: https://pypi.python.org/pypi/unilog
.. |PyVersions| image:: https://img.shields.io/pypi/pyversions/unilog.svg
    :target: https://pypi.python.org/pypi/unilog
.. |PyImplementations| image:: https://img.shields.io/pypi/implementation/unilog.svg
    :target: https://pypi.python.org/pypi/unilog
.. |Status| image:: https://img.shields.io/travis/oleg-golovanov/unilog.svg
    :target: https://travis-ci.org/oleg-golovanov/unilog
.. |Coverage| image:: https://img.shields.io/coveralls/oleg-golovanov/unilog.svg
    :target: https://coveralls.io/github/oleg-golovanov/unilog
.. |License| image:: https://img.shields.io/github/license/oleg-golovanov/unilog.svg
    :target: https://github.com/oleg-golovanov/unilog/blob/master/LICENSE
