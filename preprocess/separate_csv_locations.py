# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file = "../marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_07_to_06_08.csv"
write_file_with_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_june/with_locations/marawi_tweets_with_locations_06_07_to_06_08.csv"
write_file_with_no_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_june/no_locations/marawi_tweets_with_no_locations_06_07_to_06_08.csv"

#--------------------------------------------------------------------------------------------------
def write_new_csv_with_locations(read_path, write_path1, write_path2):
    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        i = 1;
        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
            	print(row[5])
            	data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
                if row[5] in (None, ""):
                	print("no locations", i)
                	file_writer_2.writerow(data)
                else:
					print("location found", i)
					file_writer_1.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------
write_new_csv_with_locations(read_file, write_file_with_locations, write_file_with_no_locations)