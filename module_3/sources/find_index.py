files = ['video.avi', 'audio.mp3', 'document.do', 'folder', 'backup.tar.gz']

# for file in files:
#     index = file.find('.')
#     if index != -1:
#         suffix = file[index+1:]
#         print(f"File: {file} index: {index} suffix: {suffix}")
#     else:
#         print(f"File: {file}  suffix: not found")

for file in files:
    try:
        index = file.rindex('.')
        suffix = file[index+1:]
        print(f"File: {file} index: {index} suffix: {suffix}")
    except ValueError:
        print(f"File: {file}  suffix: not found")


