#!/usr/bin/env python3

import pathlib

from setuptools import setup, find_packages


setup(
    name="pasta",
    author="",
    version="0.0.1",
    url="",
    license="",
    description="",
    install_requires=pathlib.Path('requirements.txt').read_text().splitlines(),
    packages=find_packages(),
    scripts=['bin/pasta-gunicorn'],
    entry_points={
        'console_scripts': ['pasta = pasta:main']
    },
)
