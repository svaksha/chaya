from setuptools import setup
import os
import chaya

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='chaya',
      version = chaya.__version__,
      description ='Learn computer vision, edge detection',
      long_description = readme(),
      packages = ['chaya'],
      author = 'SVAKSHA',
      author_email = 'svaksha@gmail.com',
      url = 'https://github.com/svaksha/chaya',
      install_requires = ['Cython==0.19.1',
                          'Pillow==2.1.0',
                          'distribute==0.6.34',
                          'numpy==1.7.1',
                          ],
      classifiers=[
        'Development Status :: 13.08 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: AGPLv3 License',
        'Programming Language :: Python :: 3.3',
        'Topic :: Graphics :: Computer Vision',
        ],
      packages=['chaya', 'chaya.tests'], #TODO
      )

