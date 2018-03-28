#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='random_variable',
      version='0.2',
      description='A library for computing expectation values',
      author='Massimo DiPierro',
      author_email='massimo.dipierro@gmail.com',
      long_description=open("README.md").read(),
      url='https://github.com/mdipierro/random_variable',
      install_requires=[],
      py_modules=["random_variable"],
      license= 'BSD',
      package_data = {'': ['README.md']},
      keywords='expectation values random variables'
      )
