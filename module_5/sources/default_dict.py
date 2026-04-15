
# text = """Hello my dear friend! Welcome to sources folder. I wish you good luck"""

# def get_words_list(text):
#     words_list = text.split(' ')
#     word_dict = {}
#     for i in words_list:
#         word = word_dict.get(i[0])
#         if word:
#             word.append(i)
#         else:
#             word_dict[i[0]] = [i]
#     print(word_dict)

# get_words_list(text)

######## alternative to the previous 
from collections import defaultdict

text = """Hello my dear friend! Welcome to sources folder. I wish you good luck"""

def get_words_list(text):
    word_dict = defaultdict(list)
    words_list = text.split(' ')
    for i in words_list:
        word_dict[i[0]] = i
    print(word_dict)

get_words_list(text)
