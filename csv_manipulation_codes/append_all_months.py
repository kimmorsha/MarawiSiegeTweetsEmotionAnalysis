# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file1 = '../dataset/01_may/marawi_tweets_may.csv'
read_file2 = '../dataset/02_june/marawi_tweets_june.csv'
read_file3 = '../dataset/03_july/marawi_tweets_july.csv'
read_file4 = '../dataset/04_august/marawi_tweets_august.csv'
read_file5 = '../dataset/05_september/marawi_tweets_september.csv'
read_file6 = '../dataset/06_october/marawi_tweets_october.csv'

write_file = '../dataset/marawi_tweets.csv'

#--------------------------------------------------------------------------------------------------
def append_by_month(read_path1, read_path2, read_path3, read_path4, read_path5, read_path6, write_path):
    with open (write_path, 'wb') as outFile:
        file_writer = csv.writer(outFile)

        with open(read_path1,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path2,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path3,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path4,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path5,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path6,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

#-----------------------------------------------------------------------------------------------------
append_by_month(read_file1, read_file2, read_file3, read_file4, read_file5, read_file6, write_file)


