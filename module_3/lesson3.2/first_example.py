string = '      Hello, world!       \n'

print(string)

stripped_string = string.strip()
print(stripped_string)

# string = 'apple,banana,  mango, orange'
# fruits = string.split(',')
# print(fruits)
# for fruit in fruits:
#     print(fruit.strip(), end=',')

string = 'apple,banana,mango,orange'
fruits = string.split(',')
print(fruits)
# new_string = '\t'.join(fruits)
# print(new_string)

def custom_join(spec_list,separator):
    return f'{separator}'.join(spec_list)

print(custom_join(fruits, '---'))
