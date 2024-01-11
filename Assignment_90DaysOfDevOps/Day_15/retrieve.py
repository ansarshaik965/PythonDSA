import json

with open("service.json", 'r') as file:
        data = json.load(file)
#print(data)

for key in data['services']:
    print(key,":",data['services'][key]['name'])