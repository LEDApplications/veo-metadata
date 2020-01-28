#!/usr/env/bin python

from utils import read_csv, write_json


def format_simple_occ(pretty=False):
    print("Creating two digit occupation codes")
    csv_file = '../raw/label_dod_occ_code_simple.csv'
    json_file = '../out/label_dod_occ_code.json'

    csv_data = []
    for i, row in enumerate(read_csv(csv_file)):
        if 'X' in row['dod_occ_code']:
            dod_id = row['dod_occ_code']
            label = row['label']
            csv_data.extend([{"id": dod_id, "label": label}])

    write_json(csv_data, json_file, "labels", pretty)

