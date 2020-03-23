# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# isbnlib-porbase -- an isbnlib plugin for porbase (urn.porbase.org Portugal)
# Copyright (C) 2018-2019  Alexandre Lima Conde

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from isbnlib_porbase import __version__

setup(
    name='isbnlib-porbase',
    version=__version__,
    author='xlcnd',
    author_email='xlcnd@outlook.com',
    url='https://github.com/xlcnd/isbnlib-porbase',
    download_url='https://github.com/xlcnd/isbnlib-porbase/archive/v1.0.0.zip',
    packages=['isbnlib_porbase/'],
    entry_points={'isbnlib.metadata': ['porbase=isbnlib_porbase:query']},
    install_requires=["isbnlib>=3.9.1,<3.11.0"],
    license='LGPL v3',
    description='A plugin for isbnlib that pulls metadata from porbase (urn.porbase.org Portugal).',
    long_description=open('README.rst').read(),
    keywords='ISBN isbnlib porbase bibliographic-references',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
