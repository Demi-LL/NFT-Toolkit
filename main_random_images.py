from utils.RandomImages import RandomImages

filepath = input('Input filepath you want to read:')
writepath = input('Input filepath you want to write:')
rename_folder = input('Input folder pather you want to save rename files(default rename/):') or 'rename/'

random_images = RandomImages()
random_images.set_read_filepath(filepath)
random_images.set_write_filepath(writepath)
random_images.set_rename_folder(rename_folder)

random_images.write_random_filenames()
random_images.rename_random_files()
