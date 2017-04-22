"""
Sean Smith and Vivianna Yee

Point in Polygon Algorithm using Yices
Decides if a Lat/long pair is contained in a polygon

See http://erich.realtimerendering.com/ptinpoly/

"""

import json
import geojson
import subprocess
import os
import pprint
import time


with open('boston_censustracts.geojson') as data_file:
    data = json.load(data_file)
    geo = geojson.FeatureCollection(data["features"])

def cta(lat, lng, path):
    for feature in geo['features']:
        multipolygon = feature["geometry"]["coordinates"]
        is_multipolygon = feature["geometry"]["type"] == "MultiPolygon"
        if in_polygon(lat, lng, multipolygon, is_multipolygon):
            return feature["properties"]
    return {'NTACode': 'Not Found', 'BoroName': 'Not Found'}

def x(lnglat):
    return lnglat[0]

def y(lnglat):
    return lnglat[1]

def in_polygon(lat, lng, polygon, is_multipolygon):
    for coord in polygon:
        if is_multipolygon:
            coord = coord[0]
        c = False
        j = len(coord) - 1;
        for i in range(len(coord)):
            px = lng
            py = lat
            if ( ((y(coord[i])>py) != (y(coord[j])>py)) and 
                (px < (x(coord[j])-x(coord[i])) * (py-y(coord[i])) / (y(coord[j])-y(coord[i])) + x(coord[i])) ):
                c = not c
            j = i
        if c:
            return True
    return False


def test():

    with open("mbta.json", "r") as routes:
        routes = json.load(routes)
        for route in routes:
            for stop in routes[route]['path']['direction']:
                for coord in stop['stop']:
                    lat = float(coord['stop_lat'])
                    lng = float(coord['stop_lon'])
                    name = coord['stop_name']
                    start = time.time()
                    print "%s (%f, %f)" % (name, lat, lng)
                    result = cta(lat, lng, 'boston_censustracts.geojson')
                    if 'namelsad10' in result:
                        print result['namelsad10']
                    else:
                        print "Not in Boston!"
                    stop = time.time()
                    print "Took %f seconds." % (stop-start)

    # print "Movie Theater (%f, %f)" % (42.34554065455048, -71.10334396362305)
    # print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson')['namelsad10'])

    # print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
    # print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson')['namelsad10'])

    # print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
    # print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')['namelsad10'])

if __name__ == '__main__':
    test()
