# RUN IN PYTHON 3
import json
import requests

# API url for obesity data for Boston only
cdc_url = 'https://chronicdata.cdc.gov/resource/ahrt-wk9b.json?$offset=13908&$limit=177'

response = requests.get(cdc_url)
data = response.json()
result = {}

for item in data:
    lon = item['geolocation']['longitude']
    lat = item['geolocation']['latitude']
    result[item['uniqueid']] = {'long': float(lon), 'lat': float(lat)}

with open('obese.json', 'w') as f:
    json.dump(result, f)

print('Finished get_obese.py')