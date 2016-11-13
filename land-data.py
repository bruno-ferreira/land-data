#!/usr/bin/env python
"""land-data.py: Loads GeoJSON data into a PostgreSQL database"""

import os
import json


def get_land_files():
    """ Get all list of all the geojson files """
    for file in os.listdir('./data/'):
        if file.endswith('.geojson'):
            yield(os.path.realpath(file))


f = get_land_files()
for file2 in f:
    print(file2)
