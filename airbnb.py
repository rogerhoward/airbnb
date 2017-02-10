#!/usr/bin/env python

import os, sys, csv
import requests
from pprint import pprint
import simplejson as json
import datetime

def get():
    more = True
    offset = 0
    page_size = 50
    results = []

    while more:
        print('fetching {} to {}'.format(offset, offset + page_size))
        try:
            response = requests.get(
                url="https://api.airbnb.com/v2/search_results",
                params={
                    "client_id": "3092nxybyb0otqw18e8nh5nty",
                    "locale": "en-US",
                    "currency": "USD",
                    "_format": "for_search_results",
                    "_limit": str(page_size),
                    "_offset": str(offset),
                    "fetch_facets": "false",
                    "ib": "false",
                    "ib_add_photo_flow": "true",
                    "location": "Long Beach, CA, US",
                    "sort": "1",
                },
            )

            if response.status_code == 200:
                results.extend(response.json()['search_results'])
                offset += page_size
            else:
                return results

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    return results


def save(records):
    os.makedirs('./_data', exist_ok=True)
    path = './_data/{:%Y%m%d_%H%M%S}.json'.format(datetime.datetime.now())

    with open(path, 'w') as f:
        json.dump(records, f, indent=4, ensure_ascii=False, sort_keys=True)

    return path


results = get()
saved = save(results)

pprint(saved)
pprint('--------------------------------------------------')
print('items: {}'.format(len(results)))