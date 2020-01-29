#!/usr/env/bin python

from utils import read_csv, write_json


def format_paygrade(file_name, label_column, pretty=None):
    print("Creating {} labels".format(label_column))
    csv_file = '../raw/{}.csv'.format(file_name)
    json_file = '../out/{}.json'.format(file_name)
    json_file_groups = '../out/{}_groups.json'.format(file_name)

    # handle the non-grouped paygrades
    csv_data = []
    csv_data_groups = []
    csv_data_dict = {}
    csv_data_groups_dict = {}
    for i, row in enumerate(read_csv(csv_file)):
        veo_id = row[label_column]
        label = row['label']

        if "-" not in veo_id:
            csv_data_dict[veo_id] = label
            csv_data.extend([{"id": veo_id, "label": label}])

        else:
            label_split = veo_id.split("-")
            csv_data_groups_dict[veo_id] = {'max': max(label_split), 'min': min(label_split)}

    for key in csv_data_groups_dict.keys():
        append_text = ''
        if csv_data_groups_dict[key]['max'] == 'E5':
            append_text = 'and below'
            label = 'E5'
        elif csv_data_groups_dict[key]['min'] == 'E6':
            append_text = 'and above'
            label = 'E6'
        else:
            print("ERROR: unexpected paygrade group: {}".format(key))
        csv_data_groups.extend([{"id": key, "label": "{} {}".format(csv_data_dict[label], append_text)}])

    write_json(csv_data, json_file, "labels", pretty)
    write_json(csv_data_groups, json_file_groups, "labels", pretty)
