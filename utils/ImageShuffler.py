import os
import re
import csv
import random

class ImageShuffler:
    CUSTOM_COLUMN = 'random'

    def __init__(self):
        self.csv_info = []
        self.column_fields = [self.CUSTOM_COLUMN]

    def set_read_filepath(self, path):
        self.filepath = path

    def set_write_filepath(self, path):
        self.writepath = path

    def set_rename_folder(self, path):
        self.rename_folder = path

    def write_random_filenames(self):
        with open(self.filepath) as f:
            self.column_fields += next(csv.reader(f))
            f.seek(0)
            for row in csv.DictReader(f):
                self.csv_info.append(row)

        random.shuffle(self.csv_info)
        for key, item in enumerate(self.csv_info):
            # 移除副檔名
            item[self.CUSTOM_COLUMN] = '{}'.format(key)
            # 保留副檔名
            # '{}.{}'.format(key, re.match(r'\w*\.(.*)', item['filename']).group(1))

        with open(self.writepath, 'w+') as f:
            writer = csv.DictWriter(f, fieldnames=self.column_fields)
            writer.writeheader()
            writer.writerows(self.csv_info)

    def rename_random_files(self):
        with open(self.writepath) as f:
            if not os.path.isdir(self.rename_folder):
                os.makedirs(self.rename_folder)
            for row in csv.DictReader(f):
                src = 'images/{}'.format(row['filename'])
                rename = '{}{}'.format(self.rename_folder, row[self.CUSTOM_COLUMN])
                os.system('cp {} {}'.format(src, rename))
