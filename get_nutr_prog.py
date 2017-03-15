# RUN IN PYTHON 3
import json
import requests

# API url for nutrition program data
data_url = 'https://data.cityofboston.gov/resource/ahjc-pw5e.json?$$app_token=XCBDEOphCK06DYmEIHveiKynh'

response = requests.get(data_url)
data = response.json()
result = {}

for item in data:
    # Filter out data without location data
    if 'location' in item and 'coordinates' in item['location']:
        lon = item['location']['coordinates'][1]
        lat = item['location']['coordinates'][0]
        result[item['name']] = {'long': float(lon), 'lat': float(lat)}

with open('programs.json', 'w') as f:
    json.dump(result, f)

print('Finished get_nutr_prog.py')