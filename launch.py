import json

with open('data.json', 'wr') as file:
    data = json.load(file)

# 'data' is now a Python dictionary or list
print(data)
