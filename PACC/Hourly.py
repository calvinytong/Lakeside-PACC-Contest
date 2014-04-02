import csv,nltk
from datetime import datetime

with open('phailin_tweets.csv', 'rU') as filein:
	read = csv.reader(filein, delimiter=',')
	writer = csv.writer(open('output.csv', 'wb'), delimiter=',')
	counter = 0
	for row in read: 
		hashtag = row[7]
		lowercase = hashtag.lower()
		if lowercase.count("#cyclonephailin") > 0:
			writer.writerow(row)

with open('output.csv', 'rU') as file:
        hourly = {}
        read = csv.reader(file)
        for data in read:
        	#strftime is time -> String
        	#strptime is string -> time
            #current = datetime.strptime(data[2], '%m/%d/%y %H:%M') #creates string from time
            current = datetime.strptime(data[2], '%m/%d/%Y %H:%M') #YEAR MUST BE CAPITALIZED 
            byhour = datetime.strftime(current, '%y/%m/%d %H') #creates time from string
            if byhour in hourly:
                    hourly[byhour] += 1
            else:
                    hourly[byhour] = 1
print hourly
#writer.writerow(hourly)

for date in hourly
	print date





						
