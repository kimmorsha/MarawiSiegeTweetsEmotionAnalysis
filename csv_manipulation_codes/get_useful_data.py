# -*- coding: utf-8 -*-

import csv
import string

#--------------------------------------------------------------------------------------------------
def get_useful_data(read_path1, write_path):
    with open (write_path, 'wb') as outFile:
        file_writer = csv.writer(outFile)

        with open(read_path1,'r') as inFile:
            file_reader = csv.reader(inFile)
            
            rownum = 0

            for row in file_reader:
              if rownum == 0:
                data = [row[1],
                      row[3],
                      row[4],
                      row[5],
                      row[6],
                      row[13]] 
                file_writer.writerow(data)
                rownum = 1

              else:
                # replace emotion with number
                # emo = row[13]
                # em = 0

                # if emo == 'anger':
                #   em = 1
                # elif emo == 'sadness':
                #   em = 2
                # elif emo == 'joy':
                #   em = 3
                # elif emo == 'fear':
                #   em = 4
                # elif emo == 'disgust':
                #   em = 5

                data = [row[1],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[13]] 

                file_writer.writerow(data)

#------------------------------------------------------------------------------------

read_file = '../dataset/marawi_tweets_final.csv'
write_file = '../dataset/marawi_dataset.csv'


get_useful_data(read_file, write_file)
