#!/usr/bin/env python3
"""land-data.py: Loads GeoJSON data into a PostgreSQL database"""

import os
import json


def get_land_files():
    """ Get all list of all the geojson files """
    for file in os.listdir('./data/'):
        if file.endswith('.geojson'):
            yield(os.path.realpath(file))


def import_json_file(file):
    """

    :param file:
    :return:
    """
    with open(file) as json_file:
        json_data = json.load(json_file)
        print(json_data)


f = get_land_files()
for file2 in f:
    print(file2)
    import_json_file(file2)
