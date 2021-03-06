import six

from six import print_

from transliterate.tests.defaults import PRINT_INFO

__title__ = 'transliterate.tests.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'


def print_info(func):
    """Print some useful info."""
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print_('\n{0}'.format(func.__name__))
        print_('============================')
        print_('""" {0} """'.format(func.__doc__.strip()))
        print_('----------------------------')
        if result is not None:
            try:
                print_(result)
            except Exception as err:
                print_(result.encode('utf8'))

        return result
    return inner


def py2only(func):
    """Skip the test on Python 3."""
    if not six.PY3:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy
