from __future__ import (absolute_import, division, print_function, unicode_literals)
################################################################################
"""
COPYRIGHT: 2012-Now, SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All copies must retain this permission notice with the copyright notice.
"""
################################################################################
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2012-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.08.dev"

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
      author=AUTHOR,
      author_email = 'svaksha@gmail.com',
      url = 'https://github.com/svaksha/chaya',
      description ='Learning computer vision, edge detection',
      long_description = open('README.rst').read()
      license = ('AGPL'),
      packages=['chaya'],
      package_data={'chaya': ['LICENSE.rst',
                              'AUTHORS.rst',
                              'README.rst',
                              ]},
      include_package_data = True,
      install_requires = ['Cython==0.19.1',
                          'Pillow==2.1.0',
                          'numpy==1.7.1',
                          'bottle==0.11.6',
                          'h5py==2.2.0',
                          'numba==0.10.0',
                          'pandas==0.12.0',
                          'plotly==0.5',
                          'requests==2.0.0',
                          'scipy==0.12.0',
                          ],
      classifiers = ['Development Status :: 13.10 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: AGPLv3 License',
                     'Programming Language :: Python :: 2.7, 3.3',
                     'Topic :: Graphics :: Computer Vision',
                     ],
      packages = ['chaya',
                  'chaya.core',
                  'chaya.datum',
                  'chaya.tests', #TODO
                  ],
      )

