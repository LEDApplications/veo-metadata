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
def write_json(data, json_file, json_obj_name, pretty):
    with open(json_file, "w", encoding='utf8') as f:
        if pretty:
            json_array = json.dumps(data,
                                    sort_keys=False,
                                    indent=4,
                                    separators=(',', ': '),
                                    ensure_ascii=False)
            json_object = '{{"{}":{}}}'.format(json_obj_name, json_array)
            f.write(json_object)
        else:
            f.write('{{"{}":{}}}'.format(json_obj_name, json.dumps(data)))
