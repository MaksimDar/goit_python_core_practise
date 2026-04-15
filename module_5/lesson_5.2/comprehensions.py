### LIST
print([i for i in range(10)])
print([pow(i,i) for i in range(10) if i % 2])
### DICT
print({i:pow(i,i) for i in range(10) if i % 2})
### SET
print({i for i in range(10)})