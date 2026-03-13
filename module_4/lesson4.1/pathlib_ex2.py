# from pathlib import Path

# file_name = Path('./Temp')
# try: 

#     file = open(file_name / 'jokes.txt', 'r', encoding='utf-8')

#     try :
#         while True:
#             line = file.readline()
#             if not line:
#                 break
#             print(line, end='')
#     except OSError:
#         print("File is nor reading")
#     finally:
#         file.close()
# except OSError:
#     print("OSError")


########### analogy to first version

from pathlib import Path

file_name = Path('./Temp')
try: 

    with open(file_name / 'jokes.txt', 'r', encoding='utf-8') as file:
       for line in file:
           print(line, end='')
except Exception as e:
    print(f"{e} with file")



