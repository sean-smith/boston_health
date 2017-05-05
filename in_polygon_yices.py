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

def write_to_file(str):
    with open("test.ys", "a") as f:
        f.write(str + "\n")

def check():
    bashCommand = "/home/ubuntu/yices-2.5.2/bin/yices test.ys" 
    p = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if "unsat" in out:
        return False
    if "sat" in out:
        return True
    return False


def in_polygon(lat, lng, polygon, is_multipolygon):
    for coord in polygon:
        if is_multipolygon:
            coord = coord[0]
        c = False
        j = len(coord) - 1;
        for i in range(len(coord)):
            write_to_file("(define y1::real)")
            write_to_file("(define y2::real)")
            write_to_file("(define x1::real)")
            write_to_file("(define x2::real)")
            write_to_file("(define px::real)")
            write_to_file("(define py::real)")

            write_to_file("(assert (= y1 %f))" % (y(coord[i])))
            write_to_file("(assert (= y2 %f))" % (y(coord[j])))

            write_to_file("(assert (= x1 %f))" % (x(coord[i])))
            write_to_file("(assert (= x2 %f))" % (x(coord[j])))

            write_to_file("(assert (= py %f))" % (lat))
            write_to_file("(assert (= px %f))" % (lng))

            write_to_file("(assert (and (or (and (< py y1) (> py y2)) (and (< py y2) (> py y1))) (or (< px x1) (< px x2))))")
            write_to_file("(check)")

            j = i
            result = check()
            if result:
                c = not c

            # delete file
            os.remove("test.ys")
        
        if c:
            return True
    return False


def test(args):
    try:
        os.remove("test.ys")
    except:
        pass

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
        print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson')['namelsad10'])

        print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
        print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson')['namelsad10'])

        print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
        print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')['namelsad10'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Determine census tract of coordinate pairs.')
    parser.add_argument('--test', dest='test', const=True, nargs='?', help='run test cases')
    parser.add_argument('--lat', dest='lat', type=float, help='latitude')
    parser.add_argument('--long', dest='long', type=float, help='longitude')

    args = parser.parse_args()
    test(args)
