import json

file = open('../static/weapons.json', 'r', encoding="utf-8_sig")
data = json.load(file)

print(data)