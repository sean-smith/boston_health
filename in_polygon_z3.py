"""
Sean Smith and Vivianna Yee

Point in Polygon Algorithm
Decides if a Lat/long pair is contained in a polygon

See http://erich.realtimerendering.com/ptinpoly/

"""

from z3 import *
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
    # for coord in polygon:
    #     if is_multipolygon:
    #         coord = coord[0]

    #     # x1 = Real('x1')
    #     # y1 = Real('y1')
    #     j = len(coord) - 1
        
    #     px = RealVal(lng)
    #     py = RealVal(lat)

    #     # i = Int('i')

    #     # s.add(ForAll([i], And(i < len(coord), i >= 0, True)))

    #     for z in range(len(coord)):
    #         s = Solver()
    #         x1 = x(coord[z])
    #         y1 = y(coord[z])
    #         x2 = x(coord[j])
    #         y2 = y(coord[j])

    #         x_t = Real('x_t')
    #         y_t = Real('y_t')
    #         x_u = Real('x_u')
    #         y_u = Real('y_u')
    #         t = Real('t')
    #         u = Real('u')

    #         s.add(x_t == px + t)
    #         s.add(y_t == py)
    #         s.add(x_u == (x2 - x1) * u + x1)
    #         s.add(x_u == (y2 - y1) * u + y2)
    #         s.add(x_t == x_u)
    #         s.add(y_t == y_u)
    #         s.add(t > 0)
    #         s.add(And(0 <= u, u <= 1))
    #         s.add(Or(And(py < y1, y2 < py), And(py < y2, y1 < py)), True)
    #         j = z

    #     if s.check() == sat:
    #         return True
    # return False

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

            s.add(Or(And(py < y1, py > y2, True), And(py < y2, py > y1, True), True))
            s.add(Or(px < x1, px < x2), True)
            s.add(py == lat, px == lng)

            j = i

            if s.check() == sat:
                c = not c
    
        if c:    
            return True
    return False

# def in_polygon(lat, lng, polygon, is_multipolygon):
#     for coord in polygon:
#             if is_multipolygon:
#                     coord = coord[0]
#             c = False
#             j = len(coord) - 1;
#             for i in range(len(coord)):
#                     px = lng
#                     py = lat
#                     if ( ((y(coord[i])>py) != (y(coord[j])>py)) and
#                             (px < (x(coord[j])-x(coord[i])) * (py-y(coord[i])) / (y(coord[j])-y(coord[i])) + x(coord[i])) ):
#                             c = not c
#                     j = i
#             if c:
#                     return True
#     return False


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
