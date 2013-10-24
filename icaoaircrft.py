# encoding: utf-8

import anydbm
import pickle
import requests
from lxml import etree
from io import StringIO
from time import sleep


label_mapping = {
    'Manufacturer': 'manufacturer',
    'Model': 'model',
    'Type Designator': 'type_code',
    'Description': 'description',
    'Engine Type': 'engine_type',
    'Engine Count': 'engine_count',
    'WTC': 'wake_category',
    'Photo': 'photo'
}

cache_path = 'icaoaircrft_cache'


class HTTPException(Exception):
    """Exception raised for errors in HTTP communication.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


def lookup(type_code='', manufacturer='', model='',
        description='', engine_count='', engine_type='',
        wake_category='', delay=0):

    if type_code is None:
        raise ValueError('type_code must not be None.')

    cache = anydbm.open(cache_path, 'c')
    if type_code in cache:
        return pickle.loads(cache[type_code])

    headers = {
        'Referer': 'http://cfapp.icao.int/Doc8643/search.cfm',
        'Cache-control': 'no-cache',
        'Pragma': 'no-cache',
        'Origin': 'http://cfapp.icao.int',
        'User-Agent': 'py-icao-aircrft'
    }
    payload = {
        'Mnfctrer': manufacturer,
        'Model': model,
        'Dscrptn': description,
        'EngCount': engine_count,
        'EngType': engine_type,
        'TDesig': type_code,
        'WTC': wake_category,
        'Button': 'Search'
    }
    url = 'http://cfapp.icao.int/Doc8643/8643_List1.cfm'
    sleep(delay)
    r = requests.post(url, headers=headers, data=payload)
    if r.status_code != 200:
        raise HTTPException('HTTP code %s returned' % r.status_code)
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(r.text), parser)
    rowcount = 0
    fieldnames = []
    data = []
    for row in tree.xpath('//tr'):
        if rowcount == 0:
            for th in row.xpath('//th/a'):
                fieldnames.append(label_mapping[th.text.strip()])
        else:
            fieldcount = 0
            record = {}
            for td in row.xpath('td'):
                if td.text is None:
                    # Field has no text
                    record[fieldnames[fieldcount]] = None
                else:
                    val = td.text.strip()
                    if val in ['', '-']:
                        val = None
                    record[fieldnames[fieldcount]] = val
                fieldcount += 1
            try:
                record['engine_count'] = int(record['engine_count'])
            except:
                pass
            data.append(record)
        rowcount += 1
    cache[type_code] = pickle.dumps(data)
    cache.close()
    return data


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Lookup ICAO aicraft data')
    parser.add_argument('-t', '--type', dest='type',
                   help='Type designator, e.g. "A319"')
    parser.add_argument('-d', '--delay', dest='delay', default="0",
                   help='Add a delay to prevent server hammering. Useful for multiple requests.')
    args = parser.parse_args()
    for item in lookup(type_code=args.type, delay=int(args.delay)):
        print item
