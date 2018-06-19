# -*- coding: utf-8 -*-

import csv
import string

no_header_file = '../dataset/marawi_tweets.csv'
with_header_file = '../dataset/marawi_tweets_final.csv'

def add_header(no_header_file, with_header_file):
	with open (with_header_file, 'wb') as outFile:
		file_writer = csv.writer(outFile)

		file_writer.writerow(["username", 
	    				 "date", 
	    				 "time", 
	    				 "tweet", 
	    				 "location",
	    				 "latitude",
	    				 "longitude",
	    				 "language",
	    				 "anger",
	    				 "joy",
	    				 "sadness",
	    				 "fear",
	    				 "disgust",
	    				 "emotion",
	    				 "percentage"])

		with open(no_header_file,'r') as inFile:
		    file_reader = csv.reader(inFile)

		    for row in file_reader:
				data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]

				file_writer.writerow(data)

add_header(no_header_file, with_header_file)