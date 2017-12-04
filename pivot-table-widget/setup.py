from __future__ import print_function

import os

from distutils.util import convert_path
from setuptools import setup, find_packages


module = 'pivot_table_widget'

meta_ns = {}
path = convert_path(module + '/__meta__.py')
with open(path) as meta_file:
    exec(meta_file.read(), meta_ns)


name = meta_ns['__name__']
version = meta_ns['__version__']
description = meta_ns['__description__']
long_description = meta_ns['__long_description__']
author = meta_ns['__author__']
author_email = meta_ns['__author_email__']
url = meta_ns['__url__']
download_url = meta_ns['__download_url__']
keywords = meta_ns['__keywords__']
license = meta_ns['__license__']
classifiers = meta_ns['__classifiers__']
include_package_data = meta_ns['__include_package_data__']
data_files = meta_ns['__data_files__']
install_requires = meta_ns['__install_requires__']
zip_safe = meta_ns['__zip_safe__']


# ref https://packaging.python.org/tutorials/distributing-packages/
setup_args = {
    'name': name,
    'version': version,
    'author': author,
    'author_email': author_email,
    'description': description,
    'long_description': long_description,
    'url': url,
    'keywords': keywords,
    'packages': find_packages(),
    'classifiers': classifiers,
    'include_package_data': include_package_data,
    'data_files': data_files,
    'install_requires': install_requires,
    'zip_safe': zip_safe,
}

setup(**setup_args)
