import os
import csv
import copy
import json
from dotenv import load_dotenv
load_dotenv()

class MetadataGenerator:
    def __init__(self):
        self.metadatas = {}

        self.init_meatadata = {
            'name': os.getenv('METADATA_NAME'),
            'description': os.getenv('METADATA_DESCRIPTION'),
            'image': 'ipfs://{}'.format(os.getenv('IPFS_CID')),
            'attributes': [],
        }

    def set_read_filepath(self, path):
        self.filepath = path
    
    def set_metadata_folder(self, folder):
        self.metadata_folder = folder or 'metadatas'

    def assemble_metadatas(self):
        self.metadatas = {}
        with open(self.filepath, 'r') as f:
            rows = csv.reader(f)
            fields = next(rows)
            for row in rows:
                metadata_name = row[0]
                metadata = copy.deepcopy(self.init_meatadata)
                metadata['name'] = '{} #{:0>3}'.format(metadata['name'], metadata_name)
                metadata['image'] = '{}/{}'.format(metadata['image'], metadata_name)
                for key, trait in enumerate(row[2:]):
                    metadata['attributes'].append({
                        'trait_type': fields[key+2],
                        'value': trait
                    })
                self.metadatas[metadata_name] = metadata

    def save_metadatas(self):
        if not os.path.isdir(self.metadata_folder):
            os.mkdir(self.metadata_folder)

        for metadata_name in self.metadatas.keys():
            with open('{}/{}'.format(self.metadata_folder, metadata_name), 'w+') as f:
                f.write(json.dumps(self.metadatas[metadata_name], indent=4))
