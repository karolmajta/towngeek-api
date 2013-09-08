# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="towngeek",
    version="0.1.6",
    package_dir={
        '': 'apps',
    },
    package_data={},
    packages=[
        'towngeek',

        'towngeek.commons',
        'towngeek.commons.api',
        'towngeek.commons.migrations',
        'towngeek.commons.serializers',

        'towngeek.locations',
        'towngeek.locations.api',
        'towngeek.locations.migrations',
        'towngeek.locations.serializers',

        'towngeek.qa',
        'towngeek.qa.api',
        'towngeek.qa.migrations',
        'towngeek.qa.serializers',

        'towngeek.ratings',
        'towngeek.ratings.api',
        'towngeek.ratings.migrations',
        'towngeek.ratings.serializers',
    ],

    install_requires=[],

    author="Karol Majta",
    author_email="karolmajta@gmail.com",
    description="Towngeek API server",
    license="MIT",
    url="http://karolmajta.com",
)
