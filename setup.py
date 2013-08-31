# -*- coding: utf-8 -*-
import sys
import subprocess

from setuptools import setup


setup(
    name="ddcs-server-stack",
    version="0.1",
    package_dir={
        'towngeek.core': 'apps/core',
    },
    package_data={},
    packages=[
        'towngeek.core',
    ],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[],

    author="Karol Majta",
    author_email="karolmajta@gmail.com",
    description="Towngeek API server",
    license="MIT",
    url="http://karolmajta.com",
)