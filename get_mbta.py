# RUN IN PYTHON 3
import json
import requests

# API url for nutrition program data
url = 'http://realtime.mbta.com/developer/api/v2/routes?api_key=JRz51UahAUCXkQHxPQ40fA&format=json'

response = urllib.request.urlopen(url).read().decode("utf-8")
response = json.loads(response)
result = {}

routes = [ mode for mode in response['mode'] if mode['mode_name'] == 'Subway' or mode['mode_name'] == 'Bus' ]
routes = [ (mode['mode_name'], route['route_id']) for mode in routes for route in mode['route'] ]

stop_url = 'http://realtime.mbta.com/developer/api/v2/stopsbyroute?api_key=JRz51UahAUCXkQHxPQ40fA'
stop_urls = {route:"{}&route={}&format=json".format(stop_url, route[1]) for route in routes}
stop_responses = {route:urllib.request.urlopen(stop_urls[route]).read().decode("utf-8") for route in stop_urls}

for route, response in stop_responses:
    stops_by_route = {}

    mode, route_id = route
    stops_by_route['mode'] = mode
    stops_by_route['path'] = json.loads(response)

    result[route_id] = stops_by_route


with open('programs.json', 'w') as f:
    json.dump(result, f)

print('Finished get_nutr_prog.py')