# Point in Polygon in Z3 and Yices

## Sean Smith, Vivianna Yee
## {swsmith, vivyee}@bu.edu

To run you'll need to install both Z3 (with python bindings) and Yices. For Z3 first download the source from [](https://github.com/Z3Prover/z3) then do the following:

	virtualenv venv
	source venv/bin/activate
	python scripts/mk_make.py --python
	cd build
	make
	make install
	# You will find Z3 and the Python bindings installed in the virtual environment
	venv/bin/z3 -h
	
	python -c 'import z3; print(z3.get_version_string())'

If successful you should see the version of z3 installed (4.5.0 for me). Next install Yices by following the instructions [here](http://yices.csl.sri.com/old/download-yices1-full.shtml). Note that the yices binary needs to be in the `PATH` environment variable. To test that it is run:

	yices

## Test Run
The script has been configured to take the following arguments:

	python in_polygon_yices.py [--test] [--lat num] [--long num]

When run with the `--test` flag, the script will run on three lat long pairs each in seperate census zones. Those test runs are:

	print "Movie Theater (%f, %f)" % (42.34554065455048, -71.10334396362305)
    print(cta(42.34554065455048, -71.10334396362305, 'boston_censustracts.geojson')['namelsad10'])

    print "Park (%f, %f)" % (42.34496971794688, -71.08823776245117)
    print(cta(42.34496971794688, -71.08823776245117, 'boston_censustracts.geojson')['namelsad10'])

    print "Fenway/Kenmore (%f, %f)" % (42.348688, -71.102873)
    print(cta(42.348688, -71.102873, 'boston_censustracts.geojson')['namelsad10'])

## Real Run

To run the script on the entire dataset run either `python in_polygon_yices.py` or `python in_polygon_z3.py`. This takes all the subway stops contained in `mbta.json` and runs the script on each of those. This is the dataset we used in our report.






