"""
Sean Smith and Vivianna Yee

Point in Polygon Algorithm
Decides if a Lat/long pair is contained in a polygon

See http://erich.realtimerendering.com/ptinpoly/

"""

import json
import geojson


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

    print "(define y1::real)"
    print "(define y2::real)"
    print "(define x1::real)"
    print "(define x2::real)"
    print "(define px::real)"
    print "(define py::real)"

    for coord in polygon:
        if is_multipolygon:
            coord = coord[0]
        c = False
        j = len(coord) - 1;
        for i in range(len(coord)):

            print "(assert (= y1 %f))" % (y(coord[i]))
            print "(assert (= y2 %f))" % (y(coord[j]))

            print "(assert (= x1 %f))" % (x(coord[i]))
            print "(assert (= x2 %f))" % (x(coord[j]))

            print "(assert (= py %f))" % (lat)
            print "(assert (= px %f))" % (lng)

            print "(assert (or (and (< py y1) (> py y2)) (and (< py y2) (> py y1))))"
            print "(assert (or (< px x1) (< px x2)))"
            

            j = i

        print "(check)"
        # print "(show-model)"

        break

        # if s.check() == sat:
        #     return True
    return False


def test():
    # lat, long 
    # 40.707438, -74.006302
    # Assuming lat = Y and long = X

    print "Movie Theater (%f, %f)" % (42.34554065455048, -71.10334396362305)
    print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson')["namelsad10"])

    print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
    print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson')["namelsad10"])

    # print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
    # print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')["namelsad10"])

if __name__ == '__main__':
    test()
