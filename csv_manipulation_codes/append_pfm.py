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
                date = str(dt.month) + str(dt.day) + str(dt.year)
                time = str(dt.hour) + str(dt.minute) + str(dt.second)
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
                date = str(dt.month) + str(dt.day) + str(dt.year)
                time = str(dt.hour) + str(dt.minute) + str(dt.second)
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
# append_csv_files(read_file1, read_file2, write_file)

# read_file1 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_24.csv'
# read_file2 = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_24.csv'
# write_file = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_24.csv'


# append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_23.csv")

# append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_24.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_25.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_26.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_26.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_26.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_27.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_27.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_27.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_28.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_28.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_28.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_29.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_29.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_29.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_30.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_30.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_30.csv")

append_csv_files("../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_31.csv")
