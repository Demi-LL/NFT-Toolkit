import os
import re
import csv
import random

CUSTOM_COLUMN = 'random'

column_fields = [CUSTOM_COLUMN]
csv_info = []
fields = []

filepath = input('Input filepath you want to read:')
write_path = input('Input filepath you want to write:')

with open(filepath) as f:
    column_fields += next(csv.reader(f))
    f.seek(0)
    for row in csv.DictReader(f):
        csv_info.append(row)

random.shuffle(csv_info)
for key, item in enumerate(csv_info):
    item[CUSTOM_COLUMN] = '{}'.format(key)
    # '{}.{}'.format(key, re.match(r'\w*\.(.*)', item['filename']).group(1))

with open(write_path, 'w+') as f:
    writer = csv.DictWriter(f, fieldnames=column_fields)
    writer.writeheader()
    writer.writerows(csv_info)

with open(write_path) as f:
    rename_folder = 'rename/'
    if not os.path.isdir(rename_folder):
        os.makedirs(rename_folder)
    for row in csv.DictReader(f):
        src = 'images/{}'.format(row['filename'])
        rename = '{}{}'.format(rename_folder, row[CUSTOM_COLUMN])
        os.system('cp {} {}'.format(src, rename))
