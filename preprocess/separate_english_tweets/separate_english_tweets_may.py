# -*- coding: utf-8 -*-

import csv
import string

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_1.csv"
# file_of_english_tweets = "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_1.csv"
# file_of_non_english_tweets = "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_1.csv"

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'wb') as outFile1, open (write_path2, 'w') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile) 
            for row in fileReader:
                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10]]

                language = row[10]

                if language == "en":
                    file_writer1.writerow(data)
                else:
                    file_writer2.writerow(data)
                i = i + 1
                print(i)

#--------------------------------------------------------------------------------------------------------


csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_23.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_24.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_30.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/initial_preprocessed/marawi_tweets_05_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_31.csv")
