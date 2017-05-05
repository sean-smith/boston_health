"""
Sean Smith and Vivianna Yee

Point in Polygon Algorithm
Decides if a Lat/long pair is contained in a polygon

See http://erich.realtimerendering.com/ptinpoly/

"""

from z3 import *
import json
import geojson
import time
import argparse

with open('boston_censustracts.geojson') as data_file:
    data = json.load(data_file)
    geo = geojson.FeatureCollection(data["features"])

def cta(lat, lng, path):
    for feature in geo['features']:
        multipolygon = feature["geometry"]["coordinates"]
        is_multipolygon = feature["geometry"]["type"] == "MultiPolygon"
        if in_polygon(lat, lng, multipolygon, is_multipolygon):
            return feature["properties"]
    return {'namelsad10': "Not in Boston!"}


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
            y1 = y(coord[i])
            y2 = y(coord[j])
            x1 = x(coord[i])
            x2 = x(coord[j])
            s = Solver()
            px = Real('px')
            py = Real('py')

            s.add(And(Or(And((py < y1), (py > y2)), And((py < y2), (py > y1))), Or((px < x1), (px < x2))))
            s.add(py == lat, px == lng)

            j = i

            if s.check() == sat:
                c = not c
    
        if c:    
            return True
    return False


def test(args):

    if args.lat and args.long:
        print "(%f, %f)" % (args.lat, args.long)
        print(cta(args.lat, args.long, 'boston_censustracts.geojson')['namelsad10'])

    elif not args.test:
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

    else:
        print "Movie Theater (%f, %f)" % (42.34554065455048, -71.10334396362305)
        print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson')["namelsad10"])

        print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
        print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson')["namelsad10"])

        print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
        print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')["namelsad10"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Determine census tract of coordinate pairs.')
    parser.add_argument('--test', dest='test', const=True, nargs='?', help='run test cases')
    parser.add_argument('--lat', dest='lat', type=float, help='latitude')
    parser.add_argument('--long', dest='long', type=float, help='longitude')

    args = parser.parse_args()
    test(args)
