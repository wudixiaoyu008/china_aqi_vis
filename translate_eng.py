import json

s = open('../city_list.json').read()
d = json.loads(s)

print (d)
