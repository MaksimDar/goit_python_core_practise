import sys

print(sys.argv)

param = sys.argv[1]
print(param)

if param.find('help') != -1:
    print('/help\n/list')

if param == '/find':
    print(f"List {sys.argv}")