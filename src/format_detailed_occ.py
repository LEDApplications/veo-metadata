#!/usr/env/bin python

from utils import read_csv, write_json


def format_detailed_occ(pretty=None):
    print("Creating detailed occupation labels")
    csv_file = '../raw/label_dod_occ_code.csv'
    json_file = '../out/label_dod_occ_code_detailed.json'

    mos_dict = {}
    occ_dict = {}

    for i, row in enumerate(read_csv(csv_file)):
        dod_id = row['dod_occ_code']
        label = row['label']
        details = "{} ({})".format(row['moc_code_label'], row['moc_code'])

        # update the mos dictionary
        if dod_id in mos_dict:
            mos_dict[dod_id] = "{}, {}".format(mos_dict[dod_id], details)
        else:
            mos_dict[dod_id] = details
        # update the occ dictionary
        if dod_id not in occ_dict:
            occ_dict[dod_id] = label

    # get all mos codes associated with the rollups e.g. 10X
    mos_rollup_dict = {}
    for mos_two in mos_dict.keys():
        if 'X' in mos_two:
            for mos_three in mos_dict.keys():
                if 'X' not in mos_three:
                    if mos_two[0:2] != mos_three[0:2]:
                        continue
                    if mos_two not in mos_rollup_dict:
                        mos_rollup_dict[mos_two] = mos_dict[mos_three]
                    else:
                        mos_rollup_dict[mos_two] = "{}, {}".format(mos_rollup_dict[mos_two], mos_dict[mos_three])

    # patch the mos_dict with the updated rollup values
    for key in mos_rollup_dict.keys():
        mos_dict[key] = mos_rollup_dict[key]

    csv_data = []
    for key in occ_dict.keys():
        if key not in mos_dict:
            print("ERROR: no mos code found for {}".format(key))
            break
        id = key
        label = occ_dict[key]
        details = mos_dict[key]
        csv_data.extend([{'id': id, 'label': label, 'details': details}])

    write_json(csv_data, json_file, "labels", pretty)
