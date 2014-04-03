import csv, nltk
from datetime import datetime

with open('phailin_tweets.csv', 'rU') as filein:
	read = csv.reader(filein, delimiter=',')
	writer = csv.writer(open('output.csv', 'wb'), delimiter=',')
	counter = 0
	for row in read: 
		hashtag = row[7]
		lowercase = hashtag.lower()
		if lowercase.count("#odisha") > 0:
			writer.writerow(row)

with open('output.csv', 'rU') as file:
        hourly = {}
        reader = csv.reader(file)
        for data in reader:
                #current = datetime.strptime(data[2], '%m/%d/%y %H:%M')
                current = datetime.strptime(data[2], '%m/%d/%y %H:%M')
                byhour = datetime.strftime(current, '%y/%m/%d %H')
                if byhour in hourly:
                        hourly[byhour] += 1
                else:
                        hourly[byhour] = 1
print hourly 





						
