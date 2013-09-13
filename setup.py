from setuptools import setup, find_packages
import os
import chaya

def read():
    with open('README.rst') as f:
        return f.readfile()

setup(name = 'chaya',
      version = chaya.__version__,
      author = 'SVAKSHA',
      author_email = 'svaksha@gmail.com',
      url = 'https://github.com/svaksha/chaya',
      description ='Learn computer vision, edge detection',
      long_description = open('README.rst').read()
      packages = ['chaya'],
      package_data = {'chaya': ['LICENSE.rst',
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
                  'chaya.tests',
                  ],   #TODO
      )


