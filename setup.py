# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages

name = 'morepath_rest_dump_load'
description = (
    'Morepath REST Demo'
)
long_description = (
    io.open('README.rst', encoding='utf-8').read() + '\n\n' +
    io.open('CHANGES.rst', encoding='utf-8').read())
version = '0.2.dev0'

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author='Morepath developers',
    author_email='morepath@googlegroups.com',
    license="BSD",
    url="https://github.com/morepath/morepath_rest_dump_load",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'morepath>=0.14',
    ],
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'webtest',
        ],
    ),
    entry_points={
        'console_scripts': [
            'morepath_rest = morepath_rest_dump_load.run:run',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
