from pathlib import Path

file_path = Path('ABC/text_data.txt')

data = ['first line', 'second line', 'third line']

####### write
# with open(file_path, 'w', encoding='utf-8') as file:
#     for line in data:
#         file.write(f"{line}\n")

##### append
# data = ['first line\n', 'second line\n', 'third line\n']
# with open(file_path, 'a') as file:
#     file.writelines(data)

