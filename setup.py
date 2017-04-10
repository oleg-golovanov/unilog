# -*- coding: utf-8 -*-


import re
import os

from setuptools import setup


DIR = os.path.dirname(__file__)


with open(os.path.join(DIR, 'unilog', '__init__.py')) as f:
    version = re.search(r'__version__\s+=\s+[\'\"]+(.*)[\'\"]+', f.read()).group(1)


setup(
    name='unilog',
    version=version,
    packages=['unilog'],
    url='https://github.com/oleg-golovanov/unilog',
    license='MIT',
    author='Oleg Golovanov',
    author_email='golovanov.ov@gmail.com',
    description='Representing complex object as unicode or simple string.',
    zip_safe=False,
    platforms='any',
    long_description=open(os.path.join(DIR, 'README.rst')).read(),
    test_suite='tests.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
