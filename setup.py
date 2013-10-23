# encoding: utf-8

from distutils.core import setup

setup(name='icao-aircrft',
      version='0.0.2',
      description='Python client for lookup of ICAO aircraft (Doc 8643) information',
      author='Marian Steinbach',
      author_email='marian@sendung.de',
      url='https://github.com/marians/py-icao-aircrft',
      py_modules=['icaoaircrft'],
      requires=[
          'requests',
          'lxml'
      ])
