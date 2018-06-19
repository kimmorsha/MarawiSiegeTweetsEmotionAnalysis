# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string
from dateutil.parser import parse

#--------------------------------------------------------------------------------------------------
def append_csv_files(read_path1, read_path2, write_path):
    with open (write_path, 'wb') as outFile:
        file_writer = csv.writer(outFile)

        with open(read_path1,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                # plit date into DATE & TIME
                dt = parse(row[1])
                date = str(dt.month) + "/" + str(dt.day) + "/"+ str(dt.year)
                time = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
                location = row[3]

                # split location and get the name of the place
                index = find_nth(location, "]", 1)
                place = location[:index]
                index_2 = find_nth(place, "[", 1)
                place = place[index_2+1:]

                # split location and get LATITUDE & LONGITUDE
                index = location.rfind(',')
                loc = location[:index]
                index_2 = loc.rfind(',')
                longitude = location[index_2+2:index]
                print(str(longitude))

                loc = location[:index_2]
                index = find_nth(location, "(", 3)
                latitude = loc[index+1:index_2]

                # split emotion and its percentage
                emo = row[10]
                index = find_nth(emo, "'", 1)
                index_2 = find_nth(emo, "'", 2)
                emotion = emo[index+1:index_2]

                index = find_nth(emo, ",", 1)
                index_2 = find_nth(emo, "]", 1)
                percentage = emo[index+2:index_2]

                data = [row[0],
                        date,
                        time,
                        row[2],
                        place,
                        latitude,
                        longitude,
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        emotion,
                        percentage] 

                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile:
        file_writer = csv.writer(outFile)

        with open(read_path2,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                # plit date into DATE & TIME
                dt = parse(row[1])
                date = str(dt.month) + "/" + str(dt.day) + "/"+ str(dt.year)
                time = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
                location = row[3]

                # split location and get the name of the place
                index = find_nth(location, "]", 1)
                place = location[:index]
                index_2 = find_nth(place, "[", 1)
                place = place[index_2+1:]

                # split location and get LATITUDE & LONGITUDE
                index = location.rfind(',')
                loc = location[:index]
                index_2 = loc.rfind(',')
                longitude = location[index_2+2:index]
                print(str(longitude))

                loc = location[:index_2]
                index = find_nth(location, "(", 3)
                latitude = loc[index+1:index_2]

                # split emotion and its percentage
                emo = row[10]
                index = find_nth(emo, "'", 1)
                index_2 = find_nth(emo, "'", 2)
                emotion = emo[index+1:index_2]

                index = find_nth(emo, ",", 1)
                index_2 = find_nth(emo, "]", 1)
                percentage = emo[index+2:index_2]

                data = [row[0],
                        date,
                        time,
                        row[2],
                        place,
                        latitude,
                        longitude,
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        emotion,
                        percentage]

                file_writer.writerow(data)

#-----------------------------------------------------------------------------------------------------
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
#-----------------------------------------------------------------------------------------------------

# read_file1 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_24.csv'
# read_file2 = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_24.csv'
# write_file = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_24.csv'

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_01.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_01.csv",
                   "../../dataset/03_july/marawi_tweets_07_01.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_02.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_02.csv",
                   "../../dataset/03_july/marawi_tweets_07_02.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_03.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_03.csv",
                   "../../dataset/03_july/marawi_tweets_07_03.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_04.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_04.csv",
                   "../../dataset/03_july/marawi_tweets_07_04.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_05.csv",
                   "../../dataset/03_july/marawi_tweets_07_05.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_06.csv",
                   "../../dataset/03_july/marawi_tweets_07_06.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_07.csv",
                   "../../dataset/03_july/marawi_tweets_07_07.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_08.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_08.csv",
                   "../../dataset/03_july/marawi_tweets_07_08.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_09.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_09.csv",
                   "../../dataset/03_july/marawi_tweets_07_09.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_10.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_10.csv",
                   "../../dataset/03_july/marawi_tweets_07_10.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_11.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_11.csv",
                   "../../dataset/03_july/marawi_tweets_07_11.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_12.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_12.csv",
                   "../../dataset/03_july/marawi_tweets_07_12.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_13.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_13.csv",
                   "../../dataset/03_july/marawi_tweets_07_13.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_14.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_14.csv",
                   "../../dataset/03_july/marawi_tweets_07_14.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_15.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_15.csv",
                   "../../dataset/03_july/marawi_tweets_07_15.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_16.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_16.csv",
                   "../../dataset/03_july/marawi_tweets_07_16.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_17.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_17.csv",
                   "../../dataset/03_july/marawi_tweets_07_17.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_18.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_18.csv",
                   "../../dataset/03_july/marawi_tweets_07_18.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_19.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_19.csv",
                   "../../dataset/03_july/marawi_tweets_07_19.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_20.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_20.csv",
                   "../../dataset/03_july/marawi_tweets_07_20.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_21.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_21.csv",
                   "../../dataset/03_july/marawi_tweets_07_21.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_22.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_22.csv",
                   "../../dataset/03_july/marawi_tweets_07_22.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_23.csv",
                   "../../dataset/03_july/marawi_tweets_07_23.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_24.csv",
                   "../../dataset/03_july/marawi_tweets_07_24.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_25.csv",
                   "../../dataset/03_july/marawi_tweets_07_25.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_26.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_26.csv",
                   "../../dataset/03_july/marawi_tweets_07_26.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_27.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_27.csv",
                   "../../dataset/03_july/marawi_tweets_07_27.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_28.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_28.csv",
                   "../../dataset/03_july/marawi_tweets_07_28.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_29.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_29.csv",
                   "../../dataset/03_july/marawi_tweets_07_29.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_30.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_30.csv",
                   "../../dataset/03_july/marawi_tweets_07_30.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/philippines_tweets/marawi_tweets_07_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_31.csv",
                   "../../dataset/03_july/marawi_tweets_07_31.csv")
