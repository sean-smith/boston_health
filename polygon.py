import pandas as pd
import numpy as np
import json
from pprint import pprint
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
	# lat, long 
	# 40.707438, -74.006302
	# Assuming lat = Y and long = X

	print "In the river (%f, %f)" % (-71.11227035522461, 42.3537235094212)
	print(cta(42.34554065455048, -71.10334396362305,'boston_censustracts.geojson')["namelsad10"])

	print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
	print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')["namelsad10"])

if __name__ == '__main__':
	test()
