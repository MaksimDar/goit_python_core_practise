from pathlib import Path

file_name = Path('.')

for element in file_name.iterdir():
    if file_name.glob('*.txt'):
        print(element)
    