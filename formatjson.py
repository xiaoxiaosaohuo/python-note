import json

with open('area.json', 'r') as f:
    data = json.load(f)

provinces = {}
cities = {}
counties = {}

for province in data:
    provinces[province['value']] = province['label']
    for city in province['children']:
        cities[city['value']] = city['label']
        for county in city['children']:
            counties[county['value']] = county['label']

result = {'provinces': provinces, 'cities': cities, 'counties': counties}

with open('ans.json', 'w',encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
