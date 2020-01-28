#!/usr/env/bin python

from utils import read_csv, write_json


def format_default(file_name, label_column, pretty=False):
    print("Creating {} labels".format(label_column))
    csv_file = '../raw/{}.csv'.format(file_name)
    json_file = '../out/{}.json'.format(file_name)

    csv_data = []
    for i, row in enumerate(read_csv(csv_file)):
        veo_id = row[label_column]
        label = row['label']
        csv_data.extend([{"id": veo_id, "label": label}])

    write_json(csv_data, json_file, "labels", pretty)
