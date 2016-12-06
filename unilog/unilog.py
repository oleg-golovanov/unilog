# -*- coding: utf-8 -*-


import misc


def as_unicode(object_):
    return misc.convert(object_)


def as_str(object_, encoding=misc.LOCALE):
    return as_unicode(object_).encode(encoding)


if __name__ == '__main__':
    import datetime
    data = [
        [
            {
                'dict1': 'dict1',
                u'dict12': u'dict12'
            },
            [
                1, 2, 3, 4, 5
            ],
            (
                'один', u'два', 'three', u'for', u'пять'
            )
        ],
        (
            5, 4, 3, 2, 1.11
        ),
        {
            'list': ['item1', 'item2', 'item3'],
            'tuple': tuple(('значение1', u'значение2', 'значение3')),
            'dict': {
                'date': datetime.date.today(),
                'datetime': datetime.datetime.now(),
                'NoneType': None
            }
        }
    ]

    print u'as_unicode: ', as_unicode(data)
    print 'as_str: ', as_str(data)
