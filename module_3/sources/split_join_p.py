# text = 'First sentence. Second sentence. Third sentence'

# list_text = text.split('.')

# print(list_text)

##########

# import re

# text = 'First sentence. Second sentence! Third sentence?'

# list_text = re.split('[\\.\\!\\?]', text)

# print(list_text)

###################
import re

text = 'First sentence.\nSecond sentence!\nThird sentence?'
print(text)

sentences = text.split("\n")
print(sentences)
new_text = 'ALALA'.join(sentences)
print(new_text)