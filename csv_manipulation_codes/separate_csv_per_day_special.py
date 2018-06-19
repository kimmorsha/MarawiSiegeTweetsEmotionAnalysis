# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

#  EDIT!!!!
read_file = './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_24_to_08_02.csv'
# write_file_with_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/with_locations/marawi_tweets_with_locations_05_29_to_05_30.csv"
# write_file_with_no_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/no_locations/marawi_tweets_with_no_locations_05_29_to_05_30.csv"

#--------------------------------------------------------------------------------------------------
def separate_csv_per_day(read_path):
    write_path1 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_24_1.csv'
    write_path2 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_25.csv'
    write_path3 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_26.csv'
    write_path4 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_27.csv'
    write_path5 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_28.csv'
    write_path6 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_29.csv'
    write_path7 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_30.csv'
    write_path8 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_31.csv'
    write_path9 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_08_01.csv'
    write_path10 = './marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_08_02_2.csv'
    
    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4, open (write_path5, 'w') as outFile5, open (write_path6, 'w') as outFile6, open (write_path7, 'w') as outFile7, open (write_path8, 'w') as outFile8, open (write_path9, 'w') as outFile9, open (write_path10, 'w') as outFile10:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        file_writer_3 = csv.writer(outFile3)
        file_writer_4 = csv.writer(outFile4)
        file_writer_5 = csv.writer(outFile5)
        file_writer_6 = csv.writer(outFile6)
        file_writer_7 = csv.writer(outFile7)
        file_writer_8 = csv.writer(outFile8)
        file_writer_9 = csv.writer(outFile9)
        file_writer_10 = csv.writer(outFile10)

        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
                date = row[1]

                # print(row[9])
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

                if "2017-07-24" in date:
                    # print("belongs in 2017-07-05")
                    file_writer_1.writerow(data)
                elif "2017-07-25" in date:
                    # print("belongs in 2017-06-06")
                    file_writer_2.writerow(data)
                elif "2017-07-26" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_3.writerow(data)
                elif "2017-07-27" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_4.writerow(data)
                elif "2017-07-28" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_5.writerow(data)
                elif "2017-07-29" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_6.writerow(data)
                elif "2017-07-30" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_7.writerow(data)
                elif "2017-07-31" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_8.writerow(data)
                elif "2017-08-01" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_9.writerow(data)
                elif "2017-08-02" in date:
                    #print("belongs in 2017-14-15")
                    file_writer_10.writerow(data)
                else:
                    print("belongs somewhere else")
                    #file_writer_3.writerow(data)


#-----------------------------------------------------------------------------------------------------
separate_csv_per_day(read_file)