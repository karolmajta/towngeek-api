# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="towngeek",
    version="0.1",
    package_dir={
        '': 'apps',
    },
    package_data={},
    packages=[
        'towngeek',
        'towngeek.core',
        'towngeek.core.api',
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