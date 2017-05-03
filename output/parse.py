

# read in files
with open('z3_2.txt', 'r') as z3, open('yizces.txt', 'r') as yices, open('results_2.csv', 'w') as results:

	z3_locations = []
	z3_times = []
	z3_census_tracts = []
	z3_count = 0
	for line in z3:
		# For location
		if (z3_count % 3) == 0:
			z3_locations.append(line.strip("\n"))
		
		# For census tract
		elif (z3_count % 3) == 1:
			z3_census_tracts.append(line.strip("\n"))

		# Time
		elif (z3_count % 3) == 2:
			z3_times.append(line.strip("\n"))

		z3_count += 1

	yices_locations = []
	yices_times = []
	yices_census_tracts = []
	yices_count = 0
	for line in yices:
		# For location
		if (yices_count % 3) == 0:
			yices_locations.append(line.strip("\n"))
		
		# For census tract
		elif (yices_count % 3) == 1:
			yices_census_tracts.append(line.strip("\n"))

		# Time
		elif (yices_count % 3) == 2:
			yices_times.append(line.strip("\n"))

		yices_count += 1


	# header
	results.write("%s, %s, %s\n" % ("Location", "Z3 Time", "Yices Time"))
	for z3_time, z3_location, yices_time in zip(z3_times, z3_locations, yices_times):
		z3_time = float(z3_time.split()[1])
		yices_time = float(yices_time.split()[1])
		location = z3_location.split("-")[0].strip(",")
		if (z3_time > 500):
			z3_time = 500
		if (yices_time > 500):
			yices_time = 500
		results.write("%s, %f, %f\n" % (location, z3_time, yices_time))


