from utils.ImageShuffler import ImageShuffler

filepath = input('Input filepath you want to read:')
writepath = input('Input filepath you want to write:')
rename_folder = input('Input folder path you want to save rename files(default rename/):') or 'rename/'

image_shuffler = ImageShuffler()
image_shuffler.set_read_filepath(filepath)
image_shuffler.set_write_filepath(writepath)
image_shuffler.set_rename_folder(rename_folder)

image_shuffler.write_random_filenames()
image_shuffler.rename_random_files()
