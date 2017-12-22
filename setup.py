#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages

if not sys.version.startswith('3.6'):
    sys.stderr.write("macupdate requires python 3.6\n")
    sys.exit(-1)

with open("README.md") as rm_file:
    long_description = rm_file.read()


setup(name='awsparams',
      version='0.0.1',
      description="A simple CLI and Library for adding/removing/renaming/copying AWS Param Store Parameters",
      long_description=long_description,
      author='BYU OIT Application Development',
      author_email='it@byu.edu',
      url='https://github.com/byu-oit/awsparams',
      packages=find_packages(),
      license="Apache 2",
      install_requires=['click'],
      zip_safe=True,
      entry_points={
          'console_scripts': ['macupdate=py_macupdate.cli:main']
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3 :: Only',
          'Natural Language :: English',
          'Topic :: Utilities'
      ]
      )
