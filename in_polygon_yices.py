"""
Sean Smith and Vivianna Yee

Point in Polygon Algorithm
Decides if a Lat/long pair is contained in a polygon

See http://erich.realtimerendering.com/ptinpoly/

"""

import json
import geojson
import subprocess
import os


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

def printf(str):
    with open("test.ys", "a") as f:
        # print str
        f.write(str + "\n")

def check():
    bashCommand = "/home/ubuntu/yices-2.5.2/bin/yices test.ys"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if "sat" in output:
        return True
    elif "unsat" in output:
        return False
    return False


def in_polygon(lat, lng, polygon, is_multipolygon):

    printf("(define y1::real)")
    printf("(define y2::real)")
    printf("(define x1::real)")
    printf("(define x2::real)")
    printf("(define px::real)")
    printf("(define py::real)")


    for coord in polygon:
        if is_multipolygon:
            coord = coord[0]
        c = False
        j = len(coord) - 1;
        for i in range(len(coord)):
            printf("(assert (= y1 %f))" % (y(coord[i])))
            printf("(assert (= y2 %f))" % (y(coord[j])))

            printf("(assert (= x1 %f))" % (x(coord[i])))
            printf("(assert (= x2 %f))" % (x(coord[j])))

            printf("(assert (= py %f))" % (lat))
            printf("(assert (= px %f))" % (lng))

            printf("(assert (and (or (and (< py y1) (> py y2)) (and (< py y2) (> py y1))) (or (< px x1) (< px x2))))")
            printf("(reset)")

            j = i

        printf("(check)")

    result = check()
    # delete file
    os.remove("test.ys")

    if result:
        return True
    return False


def test():
    # lat, long 
    # 40.707438, -74.006302
    # Assuming lat = Y and long = X
    try:
        os.remove("test.ys")
    except:
        pass

    print "Movie Theater (%f, %f)" % (42.34554065455048, -71.10334396362305)
    print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson'))

    print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
    print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson'))

    print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
    print(cta(42.348688, -71.102873, 'boston_censustracts.geojson'))

if __name__ == '__main__':
    test()
