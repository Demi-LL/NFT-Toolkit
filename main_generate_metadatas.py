from utils.MetadataGenerator import MetadataGenerator

metadata_path = input('Your metadata csv filepath:')
metadata_folder = input('Folder that you want to save your metadata files(default: metadatas):')

metadata_generator = MetadataGenerator()
metadata_generator.set_read_filepath(metadata_path)
metadata_generator.set_metadata_folder(metadata_folder)
metadata_generator.assemble_metadatas()
metadata_generator.save_metadatas()
