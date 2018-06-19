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

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_01.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_04.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_05.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_06.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_07.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_08.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_09.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_10.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_12.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_13.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_13.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_14.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_14.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_15.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_16.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_21.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_22.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_23.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_24.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_30.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_31.csv")
