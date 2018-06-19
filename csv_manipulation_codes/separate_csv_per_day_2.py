# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file = '../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_22_to_05_24.csv'

#--------------------------------------------------------------------------------------------------
def separate_csv_per_day(read_path):
    write_path1 = '../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_22.csv'
    write_path2 = '../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_23.csv'
    write_path3 = '../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24.csv'

    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2, open (write_path3, 'w') as outFile3:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        file_writer_3 = csv.writer(outFile3)
        # file_writer_4 = csv.writer(outFile4)
        # file_writer_5 = csv.writer(outFile5)
        # file_writer_6 = csv.writer(outFile6)

        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
                date = row[1]
            	# print(date)

                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9]]

                if "5/22/2017" in date:
                    print(date)
                    file_writer_1.writerow(data)
                elif "5/23/2017" in date:
                    print(date)
                    file_writer_2.writerow(data)
                elif "5/24/2017" in date:
                    print(date)
                    file_writer_3.writerow(data)

#-----------------------------------------------------------------------------------------------------
separate_csv_per_day(read_file)