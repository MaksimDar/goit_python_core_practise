# fh = open('text.txt', 'r')

# print(fh.read()) # 6
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()
# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(4)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# fh.close()


######## readline method 

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()

########### readlines method

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)

# fh.close()

# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()

# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)

# fh.close()

#### tell() and seek()

# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell()
# print(position)  # 6

# fh.seek(1)
# position = fh.tell()
# print(position)  # 1

# fh.read(2)
# position = fh.tell()
# print(position)  # 3

# fh.close()

# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)

# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

# byte_array = bytearray(b'Kill Bill')
# print(byte_array[0])
# print(ord('B'))
# byte_array[0] = ord('B')
# print(byte_array[0])
# print('\n')
# print(byte_array[5])
# print(ord('K'))
# byte_array[5] = ord('K')
# print(byte_array[5])
# print(byte_array)


# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()
# print(german_word.lower())
# print(search_word.lower())

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(german_word.casefold())
# print(search_word.casefold())

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")

# import shutil

# Створення TAR.GZ-архіву
# shutil.make_archive('practise.py', 'gztar')

### the usage of pathlib and PurePath

# from pathlib import PurePath

# directory = "/usr/bin/simple.jpg"

# p = PurePath("/usr/bin/simple.jpg")
# p = PurePath(directory)
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)


############## Path

# from pathlib import Path

# p = Path("example2.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 


############# Unite paths

# from pathlib import Path

# # Початковий шлях
# base_path = Path("/usr/bin")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# print(full_path)  # Виведе: /usr/bin/subdir/script.py

###### Transform relative path to the absolute 

# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()
# print(absolute_path)

#### use with_name

# from pathlib import Path

# origin = Path('documents/text.py')

# origin = origin.with_name('example.py')

# origin = origin.with_suffix('.js')

# print(origin)

############ read and write to text file 

# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")


# # Читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)


######## read and write to the binary file

# from pathlib import Path

# # Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Бінарні дані для запису
# data = b"Python is great!"

# # Запис байтів у файл
# file_path.write_bytes(data)

# ### read binary data
# binary_data = file_path.read_bytes()

# print(binary_data)

from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/example.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')



























