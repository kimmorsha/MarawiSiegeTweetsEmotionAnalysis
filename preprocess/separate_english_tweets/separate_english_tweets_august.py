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

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_01.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_01.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_04.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_05.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_06.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_07.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_08.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_09.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_10.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_12.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_13.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_13.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_13.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_14.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_14.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_14.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_15.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_16.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_21.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_22.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_23.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_24.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_30.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/initial_preprocessed/marawi_tweets_08_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_31.csv")
