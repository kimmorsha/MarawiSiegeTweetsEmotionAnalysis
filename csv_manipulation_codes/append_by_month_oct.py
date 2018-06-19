# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file1 = '../dataset/06_october/marawi_tweets_10_01.csv'
read_file2 = '../dataset/06_october/marawi_tweets_10_02.csv'
read_file3 = '../dataset/06_october/marawi_tweets_10_03.csv'
read_file4 = '../dataset/06_october/marawi_tweets_10_04.csv'
read_file5 = '../dataset/06_october/marawi_tweets_10_05.csv'
read_file6 = '../dataset/06_october/marawi_tweets_10_06.csv'
read_file7 = '../dataset/06_october/marawi_tweets_10_07.csv'
read_file8 = '../dataset/06_october/marawi_tweets_10_08.csv'
read_file9 = '../dataset/06_october/marawi_tweets_10_09.csv'
read_file10 = '../dataset/06_october/marawi_tweets_10_10.csv'
read_file11 = '../dataset/06_october/marawi_tweets_10_11.csv'
read_file12 = '../dataset/06_october/marawi_tweets_10_12.csv'
read_file13 = '../dataset/06_october/marawi_tweets_10_13.csv'
read_file14 = '../dataset/06_october/marawi_tweets_10_14.csv'
read_file15 = '../dataset/06_october/marawi_tweets_10_15.csv'
read_file16 = '../dataset/06_october/marawi_tweets_10_16.csv'
read_file17 = '../dataset/06_october/marawi_tweets_10_17.csv'
read_file18 = '../dataset/06_october/marawi_tweets_10_18.csv'
read_file19 = '../dataset/06_october/marawi_tweets_10_19.csv'
read_file20 = '../dataset/06_october/marawi_tweets_10_20.csv'
read_file21 = '../dataset/06_october/marawi_tweets_10_21.csv'
read_file22 = '../dataset/06_october/marawi_tweets_10_22.csv'
read_file23 = '../dataset/06_october/marawi_tweets_10_23.csv'

write_file = '../dataset/06_october/marawi_tweets_october.csv'

#--------------------------------------------------------------------------------------------------
def append_by_month(read_path1, read_path2, read_path3, read_path4, read_path5, read_path6, read_path7, read_path8,
                    read_path9, read_path10, read_path11, read_path12, read_path13, read_path14, read_path15, read_path16,
                    read_path17, read_path18, read_path19, read_path20, read_path21, read_path22, read_path23, write_path):
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

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path7,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path8, 'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path9,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path10,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path11,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path12,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path13,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path14,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path15,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path16,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path17,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path18,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path19,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path20,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path21,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path22,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path23,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)
    
#-----------------------------------------------------------------------------------------------------

append_by_month(read_file1, read_file2, read_file3, read_file4, read_file5, read_file6, read_file7, read_file8,
                read_file9, read_file10, read_file11, read_file12, read_file13, read_file14, read_file15, read_file16,
                read_file17, read_file18, read_file19, read_file20, read_file21, read_file22, read_file23, write_file)


