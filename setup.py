# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup


def main():
    setup(
        name=str('finsec'),
        description='An SDK to work with Financial data from the SEC.',
        url='http://finsec.readthedocs.org/en/latest/',
        version='0.0.0',
        platforms='linux',
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],

        packages=find_packages(exclude=('tests*',)),
        install_requires=[
            'argparse',
            'frozendict',
            'cached-property',
            'py',
            'six',
        ],
        author='Kent Wills',
        author_email='ronald.k.wills@gmail.com',
    )


if __name__ == '__main__':
    exit(main())
