import json
d1 = {"a": 1}
d2 = {2:1}
l = [1, 2.1]
t = (3,2)
s = "I am a string"

# print(json.dumps(d1))
# print(json.dumps(d2))
# print(json.dumps(l))
# print(json.dumps(t))
# print(json.dumps(s))

with open("file.json", 'w') as file:
    json.dump(d1,file)

with open('file.json', 'r') as file:
    data = json.load(file)

print(d1 is data)
print(d1,data)
