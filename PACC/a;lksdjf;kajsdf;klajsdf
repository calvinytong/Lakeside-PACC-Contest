import csv,nltk,pygmaps
from datetime import datetime

with open('phailin_tweets.csv', 'rU') as filein:
	read = csv.reader(filein, delimiter=',')
	writer = csv.writer(open('output.csv', 'wb'), delimiter=',')
	mymap = pygmaps.maps(32.8724, -80.013738, 5)
	headers = next(read, None)
	for row in read:
	#for i in range(0,4501):
		if row[8] != "":
			writer.writerow(row)
counter = 0		
with open('output.csv', 'ru') as file:
	reader = csv.reader(file)
	#for row in reader:
	for i in range (0, 1801):
		counter +=1
		lat = float(row[8])
		long = float(row[9])
		print counter
		tweetid = row[0]
		mymap.addpoint(float(row[8]), float(row[9]), row[0])
		mymap.draw("./mymap.html") 



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





						
