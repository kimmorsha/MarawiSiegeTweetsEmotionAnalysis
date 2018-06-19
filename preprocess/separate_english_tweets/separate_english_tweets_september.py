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

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_01.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_01.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_04.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_05.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_06.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_07.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_08.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_08.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_08.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_09.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_09.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_09.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_10.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_10.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_10.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_12.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_13.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_13.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_13.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_14.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_14.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_14.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_15.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_15.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_15.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_16.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_16.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_16.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_17.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_17.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_21.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_22.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_23.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_24.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_29.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_september/official/initial_preprocessed/marawi_tweets_09_30.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/english_tweets/marawi_tweets_09_30.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_september/official/non_english_tweets/marawi_tweets_09_30.csv")

