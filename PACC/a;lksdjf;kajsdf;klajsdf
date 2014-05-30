import csv,nltk,pygmaps
from datetime import datetime

with open('PACC_geotweets.csv', 'rU') as filein:
	read = csv.reader(filein, delimiter=',')
	writer = csv.writer(open('output.csv', 'wb'), delimiter=',')
	mymap = pygmaps.maps(32.8724, -80.013738, 5)
	mymap1 = pygmaps.maps(32.8724, -80.013738, 5)
	mymap2 = pygmaps.maps(32.8724, -80.013738, 5)
	mymap3 = pygmaps.maps(32.8724, -80.013738, 5)
	headers = next(read, None)
	for row in read:
		if row[9] != "":
			writer.writerow(row)

counter = 0		
with open('output.csv', 'rU') as file:
	reader = csv.reader(file)
	for row in reader:
			if counter < 10000:
					try:
						lat = float(row[9])
					except:
						lat = 0
					try:
						long = float(row[10])
					except:
						long = 0
					tweetid = row[0]
					mymap.addpoint(lat, long, row[0])
					mymap.draw("1st_10000.html") 
			if counter > 10000 and counter < 20000
					try:
						lat = float(row[9])
					except:
						lat = 0
					try:
						long = float(row[10])
					except:
						long = 0
					tweetid = row[0]
					mymap.addpoint(lat, long, row[0])
					mymap.draw("2nd_10000.html") 
			if counter > 20000 and counter <30000
			counter += 1
			print counter



		#hashtag = row[7]
		#lowercase = hashtag.lower()
		#if lowercase.count("#breaking") > 0:
			#writer.writerow(row)

#with open('output.csv', 'rU') as file:
#        hourly = {}
#        reader = csv.reader(file)
#        for data in reader:
#                current = datetime.strptime(data[2], '%m/%d/%y %H:%M')
#                byhour = datetime.strftime(current, '%y/%m/%d %H')
#                if byhour in hourly:
#                        hourly[byhour] += 1
#                else:
#                        hourly[byhour] = 1
#print hourly 





						
