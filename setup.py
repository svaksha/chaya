#!/usr/bin/env python3.3

from setuptools import setup, find_packages
import os, sys
import shutil
import warnings

import chaya

def read():
    with open('README.rst') as f:
        return f.readfile()

PKGNAME = 'chaya',
VERSION=chaya.__version__,
AUTHOR = "SVAKSHA",
AUTHOR_EMAIL = "svaksha@gmail.com",
URL = 'https://github.com/svaksha/chaya',
DESCRIPTION ='Learning computer vision, edge detection',
LONG_DESCRIPTION=open('README.rst').read()
PACKAGES=['chaya'],
PACKAGE_DATA={'chaya': ['LICENSE.rst',
                              'AUTHORS.rst',
                              'README.rst',
                              ]}

setup(name=PKGNAME,
      version=VERSION,
      maintainer=AUTHOR,
      author_email = 'svaksha@gmail.com',
      url = 'https://github.com/svaksha/chaya',
      description ='Learn computer vision, edge detection',
      long_description = open('README.rst').read()
      license = ('AGPL'),
      packages=['chaya'],
      package_data={'chaya': ['LICENSE.rst',
                              'AUTHORS.rst',
                              'MANIFEST.in',
                              'README.rst',
                              ]},
      include_package_data = True,
      install_requires = ['Cython==0.19.1',
                          'Pillow==2.1.0',
                          'numpy==1.7.1',
                          ],
      classifiers = ['Development Status :: 13.08 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: AGPLv3 License',
                     'Programming Language :: Python :: 3.3',
                     'Topic :: Graphics :: Computer Vision',
                     ],
      packages = ['chaya',
                  'chaya.chAya',
                  'chaya.tests',
                  ],   #TODO
      )


