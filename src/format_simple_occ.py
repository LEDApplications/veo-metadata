#!/usr/env/bin python

from utils import read_csv, write_json


def format_two_digit_occ():
    print("Creating two digit occupation codes")
    csv_file = '../raw/label_dod_occ_code_simple.csv'
    json_file = '../out/label_dod_occ_code.json'
    two_digit_occs = [x for x in read_csv(csv_file) if 'X' in x['dod_occ_code']]
    write_json(two_digit_occs, json_file, False)
