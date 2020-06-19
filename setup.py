#!/usr/bin/env python

from setuptools import setup, find_packages
import sys


setup(name='ppb_timing',
    version='0.1.1',
    description='A timing system for PursuedPyBear games.',
    author='Calvin Spealman',
    author_email='ironfroggy@gmail.com',
    url='https://github.com/ironfroggy/ppb_timing',
    py_modules=['ppb_timing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
    ],
    extras_require={
        'dev': [
            'pursuedpybear==0.8.0',
        ]
    }
)
