# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file1 = '../dataset/05_september/marawi_tweets_09_01.csv'
read_file2 = '../dataset/05_september/marawi_tweets_09_02.csv'
read_file3 = '../dataset/05_september/marawi_tweets_09_03.csv'
read_file4 = '../dataset/05_september/marawi_tweets_09_04.csv'
read_file5 = '../dataset/05_september/marawi_tweets_09_05.csv'
read_file6 = '../dataset/05_september/marawi_tweets_09_06.csv'
read_file7 = '../dataset/05_september/marawi_tweets_09_07.csv'
read_file8 = '../dataset/05_september/marawi_tweets_09_08.csv'
read_file9 = '../dataset/05_september/marawi_tweets_09_09.csv'
read_file10 = '../dataset/05_september/marawi_tweets_09_10.csv'
read_file11 = '../dataset/05_september/marawi_tweets_09_11.csv'
read_file12 = '../dataset/05_september/marawi_tweets_09_12.csv'
read_file13 = '../dataset/05_september/marawi_tweets_09_13.csv'
read_file14 = '../dataset/05_september/marawi_tweets_09_14.csv'
read_file15 = '../dataset/05_september/marawi_tweets_09_15.csv'
read_file16 = '../dataset/05_september/marawi_tweets_09_16.csv'
read_file17 = '../dataset/05_september/marawi_tweets_09_17.csv'
read_file18 = '../dataset/05_september/marawi_tweets_09_18.csv'
read_file19 = '../dataset/05_september/marawi_tweets_09_19.csv'
read_file20 = '../dataset/05_september/marawi_tweets_09_20.csv'
read_file21 = '../dataset/05_september/marawi_tweets_09_21.csv'
read_file22 = '../dataset/05_september/marawi_tweets_09_22.csv'
read_file23 = '../dataset/05_september/marawi_tweets_09_23.csv'
read_file24 = '../dataset/05_september/marawi_tweets_09_24.csv'
read_file25 = '../dataset/05_september/marawi_tweets_09_25.csv'
read_file26 = '../dataset/05_september/marawi_tweets_09_26.csv'
read_file27 = '../dataset/05_september/marawi_tweets_09_27.csv'
read_file28 = '../dataset/05_september/marawi_tweets_09_28.csv'
read_file29 = '../dataset/05_september/marawi_tweets_09_29.csv'
read_file30 = '../dataset/05_september/marawi_tweets_09_30.csv'


write_file = '../dataset/05_september/marawi_tweets_september.csv'

#--------------------------------------------------------------------------------------------------
def append_by_month(read_path1, read_path2, read_path3, read_path4, read_path5, read_path6, read_path7, read_path8,
                    read_path9, read_path10, read_path11, read_path12, read_path13, read_path14, read_path15, read_path16,
                    read_path17, read_path18, read_path19, read_path20, read_path21, read_path22, read_path23, read_path24,
                    read_path25, read_path26, read_path27, read_path28, read_path29, read_path30, write_path):
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

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path24,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path25,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path26,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path27,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path28,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path29,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path30,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
                file_writer.writerow(data)

    
#-----------------------------------------------------------------------------------------------------

append_by_month(read_file1, read_file2, read_file3, read_file4, read_file5, read_file6, read_file7, read_file8,
                read_file9, read_file10, read_file11, read_file12, read_file13, read_file14, read_file15, read_file16,
                read_file17, read_file18, read_file19, read_file20, read_file21, read_file22, read_file23, read_file24,
                read_file25, read_file26, read_file27, read_file28, read_file29, read_file30, write_file)


