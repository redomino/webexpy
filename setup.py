#!/usr/bin/env python
from distutils.core import setup

VERSION = '2.2.6'

tests_require = ['nose']

setup(
    name='webexpy',
    version=VERSION,
    description='Python WebEx Api Wrapper',
    author='Michael Prior',
    author_email='prior@cracklabs.com',
    url='https://github.com/prior/webexpy',
    download_url='https://github.com/prior/webexpy/tarball/v%s'%VERSION,
    packages=['webex','webex.test'],
    install_requires=['lxml', 'requests<=0.12.1', 'sanetime', 'utilspy', 'gevent'],
    tests_require=tests_require,
    extras_require = {
                      'test': tests_require,
                     },
)
