unilog
------

|Version| |PyVersions| |License|

Representing complex object as unicode or simple string.

Installation
------------
::

    $ pip install unilog

Example
-------
.. code-block:: python

    data = [
        [
            {
                'dict1': 'dict1',
                u'dict12': u'dict12'
            },
            [
                1, 2, 3, 4, 5, None
            ],
            (
                'один', u'два', 'three', u'for', u'пять', None
            )
        ],
        (
            5, 4, 3, 2, 1.11, None
        ),
        {
            'list': ['item1', 'item2', u'пункт3'],
            'tuple': tuple(('значение1', u'значение2', 'значение3')),
            'dict': {
                'date': datetime.date(2016, 12, 6),
                'datetime': datetime.datetime(2016, 12, 6, 11, 22, 33, 444444),
                'NoneType': None
            }
        }
    ]

    # default python behavior
    >>> print unicode(data)
    [[{'dict1': 'dict1', u'dict12': u'dict12'}, [1, 2, 3, 4, 5, None], ('\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd', u'\u0434\u0432\u0430', 'three', u'for', u'\u043f\u044f\u0442\u044c', None)], (5, 4, 3, 2, 1.11, None), {'dict': {'date': datetime.date(2016, 12, 6), 'NoneType': None, 'datetime': datetime.datetime(2016, 12, 6, 11, 22, 33, 444444)}, 'list': ['item1', 'item2', u'\u043f\u0443\u043d\u043a\u04423'], 'tuple': ('\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb51', u'\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u04352', '\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb53')}]

    # use unilog.as_unicode function
    >>> print unilog.as_unicode(data)
    [[{'dict1': 'dict1', u'dict12': u'dict12'}, [1, 2, 3, 4, 5, None], ('один', u'два', 'three', u'for', u'пять', None)], (5, 4, 3, 2, 1.11, None), {'dict': {'date': u'2016-12-06', 'NoneType': None, 'datetime': u'2016-12-06 11:22:33.444444'}, 'list': ['item1', 'item2', u'пункт3'], 'tuple': ('значение1', u'значение2', 'значение3')}]

License
-------
MIT licensed. See the bundled `LICENSE <https://github.com/oleg-golovanov/unilog/blob/master/LICENSE>`_ file for more details.

.. |Version| image:: https://img.shields.io/pypi/v/unilog.svg
    :target: https://pypi.python.org/pypi/unilog
.. |PyVersions| image:: https://img.shields.io/pypi/pyversions/unilog.svg
    :target: https://pypi.python.org/pypi/unilog
.. |License| image:: https://img.shields.io/github/license/oleg-golovanov/unilog.svg
    :target: https://github.com/oleg-golovanov/unilog/blob/master/LICENSE
