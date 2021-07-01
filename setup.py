#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################
import os
from setuptools import setup, find_packages
import simpleapp_adapter

def read_file(path: str):
    with open(path, "r") as file:
        return file.read()

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="geonode-simpleapp",
    version=simpleapp_adapter.__version__,
    url=simpleapp_adapter.__url__,
    description=simpleapp_adapter.__doc__,
    author=simpleapp_adapter.__author__,
    author_email=simpleapp_adapter.__email__,
    license=simpleapp_adapter.__license__,
    platforms="any",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    package_data={'':['*.html', '*.js']},
    include_package_data=True
)
