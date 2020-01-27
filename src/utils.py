import csv
import json


# Read CSV File
def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
        return csv_rows
        # write_json(csv_rows, json_file, pretty)


# Convert csv data into json and write it
def write_json(data, json_file, pretty):
    with open(json_file, "w", encoding='utf8') as f:
        if pretty:
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),
                               ensure_ascii=False))
        else:
            f.write(json.dumps(data))
