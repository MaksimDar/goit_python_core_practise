transmap = {
    ord('М'): "M",
    ord('а'): "a",
    ord('к'): "k",
    ord('с'): "s",
    ord('и'): "y",
    ord('м'): "m",
    
}

# ukr_name = 'Максим'
# en_name = 'Maksym'

# final = ukr_name.translate(transmap)

# print(ukr_name, '=', final, sep=" ")

text = 'Hello Мaksym'
index = text.find('Maksym')
#######
new_index = text.translate(transmap).find('Maksym')
print(index, '\n')

print(new_index)
