# hello = """Hello!
# How are you?
# Are you okay?"""

# print(hello)

# one_line_text = "Textual data in Python is handled with str objects," \
#                 " or strings. Strings are immutable sequences of Unicode" \
#                 " code points. String literals are written in a variety " \
#                 " of ways: single quotes, double quotes, triple quoted."


# one_line_text = ("Textual data in Python is handled with str objects,"
                
#     " or strings. Strings are immutable sequences of Unicode"
#         " code points. String literals are written in a variety "
#             " of ways: single quotes, double quotes, triple quoted.")

# print(one_line_text)


# greeting="hello\nWorld!"

# print(greeting)

# greeting3="hello\tWorld!"

# print(greeting3)

# print("Hello my little\rsister")

# print("Hello\\World")

# print('It\'s a beautiful day')
# print("He said, \"Hello\"")

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("her", start, end)) # 5
# print(s.find("q")) # -1

# s = 'Some words wonderful'

# print(s.find("o"))
# print(s.rfind('o'))

# text = "apple,banana,cherry,blackberry"
# result = text.split(',', 1)
# print(result)  # Виведе: ['apple', 'banana', 'cherry']

# elements = ['earth', 'air', 'fire', 'water']
# result = '!  '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 3)
# print(new_text)  

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

#########################
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))

# intab = "aeiou"
# trantab = str.maketrans('', '', intab)

# str = "This is string example"
# print(str.translate(trantab))

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AE".translate(MAP)
# print(result)

# for i in range(15):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)

# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)

# completion = 0.756
# formatted = f"{completion:.1%}"
# print(formatted)  # Виведе: '75.6%'

# import re

# my_string = "world@gmail.com"

# print(re.search('e|r', my_string))
# print(re.findall('l', my_string))
# print(re.sub('o', '1', my_string))

# print(re.split('e', my_string))

# print(my_string)

# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.string)
# else:
#     print("Не знайдено.")

# import re

# text = "Funny Python може бути funny."
# pattern = r"f\w*y"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())

# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())

# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

##########################
# import re

# text = "Python - це проста, 11 але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку

################################

# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)

################
# import re

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\s+"
# words = re.split(pattern, text)

# print(words)  # Виведе список слів у рядку

##############
# import re

# text = "Python - потужна; проста, універсальна: мова!"
# pattern = r"[;,\-:!\s]+"
# elements = re.split(pattern, text)

# print(elements)  # Виведе список частин, розділених пунктуацією


















