import shutil

archieve = shutil.make_archive('backup', 'zip', 'Temp/')

print(archieve)

shutil.unpack_archive(archieve, 'New_Folder')

