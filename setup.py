# -*- coding: utf-8 -*-

"""setup.py example for a new metadata provider.

   For a new formatter, it will be the same logic with 'entry_points'
   identifier equal to 'isbnlib.formatters' in a folder with name
   'isbnlib_formatter_dummy'.

   Please, upload me to pypi!
"""


from setuptools import setup


setup(
    name='isbnlib_porbase',
    version='0.0.1',
    author='xlcnd',
    author_email='xlcnd@outlook.com',
    url='_____________________________________',
    download_url='___________________________________',
    packages=['isbnlib_porbase/'],
    entry_points = {
        'isbnlib.metadata': ['porbase=isbnlib_porbase:query']
    },
    install_requires=["isbnlib>=3.7.3,<3.8.0"],
    license='LGPL v3',
    description='A plugin for isbnlib pulling metadata from porbase.org (portuguese books).',
    keywords='ISBN, porbase, isbnlib',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
