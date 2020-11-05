#!/usr/env/bin python

from utils import read_csv, write_json


def format_paygrade(file_name, label_column, pretty=None):
    print("Creating {} labels".format(label_column))
    csv_file = '../raw/{}.csv'.format(file_name)
    json_file = '../out/metadata/{}.json'.format(file_name)
    json_file_groups = '../out/metadata/{}_groups.json'.format(file_name)

    # handle the non-grouped paygrades
    csv_data = []
    csv_data_groups = []
    for i, row in enumerate(read_csv(csv_file)):
        veo_id = row[label_column]
        label = row['label']
        level = row['paygrade_level']
        paygrade = row['paygrade']

        if level == "E" or level == "A" and len(paygrade) <= 3:
            csv_data.extend([{"id": veo_id, "label": label}])

        if level == "G" or level == "A" and len(paygrade) > 3:
            csv_data_groups.extend([{"id": veo_id, "label": label}])

    write_json(csv_data, json_file, "labels", pretty)
    write_json(csv_data_groups, json_file_groups, "labels", pretty)
