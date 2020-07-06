#!/usr/bin/env python

from os.path import join
from os import linesep
from pathlib import Path
from utils import get_header_csv
import csv

REQUIRED_FIELDS = ['y1_emp', 'y5_emp', 'y10_emp', 'y1_nonemp', 'y5_nonemp', 'y10_nonemp', 'y1_p25_earnings',
                   'y5_p25_earnings', 'y10_p25_earnings', 'y1_p50_earnings', 'y5_p50_earnings', 'y10_p50_earnings',
                   'y1_p75_earnings', 'y5_p75_earnings', 'y10_p75_earnings', 'status_y1_emp', 'status_y5_emp',
                   'status_y10_emp', 'status_y1_nonemp', 'status_y5_nonemp', 'status_y10_nonemp', 'status_y1_earn',
                   'status_y5_earn', 'status_y10_earn']


def generate_appdata():
    # set output directory
    output_directory = "../out/data"

    # create output directory
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Iterate through table listing
    for table in ["veoa",
                  "veoe",
                  "veons",
                  "veoo2ns",
                  "veoo2p",
                  "veoo3",
                  "veop",
                  "veorh",
                  "veos",
                  "veot",
                  "veox"]:
        print("Processing {}...".format(table))
        csv_file = "{}.csv".format(table)
        csv_file_in = join("../raw/", csv_file)
        csv_file_out = join(output_directory, csv_file)

        # get the columns contained in the csv
        table_fields = get_header_csv(csv_file_in)

        missing_fields = [field for field in REQUIRED_FIELDS if field not in table_fields]

        with open(csv_file_in, 'r') as f_in, open(csv_file_out, 'w', newline='') as f_out:
            csv_reader = csv.reader(f_in, delimiter=',')
            writer = csv.writer(f_out, lineterminator=linesep)

            # rewrite each row to include blank values for the missing fields
            for i, row in enumerate(csv_reader):

                # if missing fields is empty, the row isn't modified
                # for the header, add the field names
                if i == 0:
                    row.extend(missing_fields)
                # all others, add empty strings
                else:
                    row.extend([""] * len(missing_fields))

                # write to the output
                writer.writerow(row)


if __name__ == "__main__":
    generate_appdata()
