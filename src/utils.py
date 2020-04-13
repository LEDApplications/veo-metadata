import csv
import json
from zipfile import ZipFile
from os.path import basename


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
def write_json(data, json_file, json_obj_name, format='pretty'):
    with open(json_file, "w", encoding='utf8') as f:
        if format == 'pretty':
            json_array = json.dumps(data,
                                    sort_keys=False,
                                    indent=4,
                                    separators=(',', ': '),
                                    ensure_ascii=False)
            json_object = '{{"{}":{}}}'.format(json_obj_name, json_array)
            f.write(json_object)
        elif format == 'minify':
            f.write('{{"{}":{}}}'.format(json_obj_name, json.dumps(data, separators=(',', ':'))))
        else:
            f.write('{{"{}":{}}}'.format(json_obj_name, json.dumps(data)))


# Create a zip file
def create_zip(outzip, *argv):
    zipobj = ZipFile(outzip, 'w')
    for arg in argv:
        zipobj.write(arg, basename(arg))

    zipobj.close()
