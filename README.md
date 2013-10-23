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

    >>> import icao-aircrft
    >>> query = 'PAY3'
    >>> for result in icao-aircrft.lookup(type_code=query):
    >>>     print result
    {'description': 'Landplane', 'wake_category': 'L', 'photo': None, 'type_code': 'PAY3', 'engine_count': 2, 'model': 'PA-42-720 Cheyenne 3', 'engine_type': 'Turboprop', 'manufacturer': 'AICSA'}
	{'description': 'Landplane', 'wake_category': 'L', 'photo': None, 'type_code': 'PAY3', 'engine_count': 2, 'model': 'Cheyenne 3', 'engine_type': 'Turboprop', 'manufacturer': 'AICSA'}
	...

