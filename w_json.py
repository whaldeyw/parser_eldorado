import json

# with open('smart.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
#     print(data)

my_file = open('smart.json','r', encoding='utf-8')

contents = my_file.read()

print(contents)

my_file.close()