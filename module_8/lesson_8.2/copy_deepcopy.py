from copy import copy,deepcopy

original_list = [1,2,[3,4,5],[4,3,2]]

copy_list = original_list
copy_list.append(3)
print(copy_list is original_list)

print(f"Copy list: {copy_list}")
print(f"Original list: {original_list}")

#### Using copy
#shallow copy
print("Shallow list")
shallow_copy_list = copy(original_list)
shallow_copy_list[2][0] = 'X'
shallow_copy_list.append(5)
print(original_list, shallow_copy_list, sep='\n')

### Using deepcopy
print("Deep list")
deep_copy = deepcopy(original_list)
deep_copy[2][0] = 'Y'
print(original_list, deep_copy, sep='\n')
