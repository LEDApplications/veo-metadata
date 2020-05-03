#!/usr/env/bin python

from utils import write_json


def format_cohort_years(start_year, end_year, years, pretty=None):
    print("Creating {} year labels".format(years))
    json_file = '../out/metadata/label_{}year_cohorts.json'.format(years)

    csv_data = []
    for x in range(start_year, end_year, years):
        veo_id = "{}".format(x)
        label = "{}-{}".format(x, x + years - 1)
        csv_data.extend([{"id": veo_id, "label": label}])

    write_json(csv_data, json_file, "labels", pretty)
