py-icao-aircrft
===============

Python client for lookup of ICAO aircraft ([Doc 8643](http://www.icao.int/publications/DOC8643/Pages/default.aspx)) information, also known as "Aircraft Type Designators".

## Install

    pip install icao-aircrft

The module requires requests and lxml to be installed.

## Usage

Example for use via the command line:

    python -m icao-aircrft -t PAY3

Example code for use as a library:

    >>> import icaoaircrft
    >>> query = 'PAY3'
    >>> for result in icaoaircrft.lookup(type_code=query):
    >>>     print result
    {'description': 'Landplane', 'wake_category': 'L', 'photo': None, 'type_code': 'PAY3', 'engine_count': 2, 'model': 'PA-42-720 Cheyenne 3', 'engine_type': 'Turboprop', 'manufacturer': 'AICSA'}
	{'description': 'Landplane', 'wake_category': 'L', 'photo': None, 'type_code': 'PAY3', 'engine_count': 2, 'model': 'Cheyenne 3', 'engine_type': 'Turboprop', 'manufacturer': 'AICSA'}
	...

## Notes

The module does not contain the actual database. Instead it issues requests online to the icao.int server.

The results of lookups are stored in a local cache file called icaoaircrft_cache.db within the current directory. This file can be deleted at any time to get rid of stale data.

Due to the way the cache file is written, the module might not be thread-safe.