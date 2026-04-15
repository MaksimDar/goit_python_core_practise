from datetime import datetime

test = datetime.now()

test_str = '12345'
test_list = [1,2,3]

print(str(test)) # 2026-04-09 15:26:56.698424
print(repr(test)) # datetime.datetime(2026, 4, 9, 15, 26, 56, 698424)

print(str(test_str)) # 12345
print(repr(test_str)) # '12345'

print(str(test_list)) # [1, 2, 3]
print(repr(test_list)) # [1, 2, 3]

print(test, test_str, test_list, sep='\n')