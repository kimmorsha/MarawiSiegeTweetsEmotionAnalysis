# -*- coding: utf-8 -*-

import csv
import string
import preprocessor as p

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open (write_path, 'wb') as outFile1:
        file_writer1 = csv.writer(outFile1)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
                cleaned_tweet = p.clean(tweet)
                print(i)
                print(cleaned_tweet)

                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        cleaned_tweet,
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9]]

                file_writer1.writerow(data)

                i = i + 1
#-----------------------------------------------------------------------------------------------------

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_01.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_04.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_05.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_06.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_06.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_07.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_07.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_08.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_09.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_10.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_12.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_13.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_13.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_14.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_14.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_15.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_16.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_21.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_22.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_22.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_23.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_24.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_30.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_october/official/initial_preprocessed/marawi_tweets_10_31.csv")