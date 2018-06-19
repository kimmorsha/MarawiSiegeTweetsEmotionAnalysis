# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file = "../../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_06_07_to_06_08.csv"
write_file_with_locations = "../../marawi_tweets_with_locations_separation/marawi_tweets_may/with_locations/marawi_tweets_with_locations_06_07_to_06_08.csv"
write_file_with_no_locations = "../../marawi_tweets_with_locations_separation/marawi_tweets_may/no_locations/marawi_tweets_with_no_locations_06_07_to_06_08.csv"

#--------------------------------------------------------------------------------------------------
def separate_no_locations(read_path, write_path1, write_path2):
    with open (write_path1, 'ab') as outFile1, open (write_path2, 'ab') as outFile2:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        i = 1;
        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
            	print(row[5])
            	data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
                if row[5] in (None, ""):
                	print("no locations", i)
                	file_writer_2.writerow(data)
                else:
					print("location found", i)
					file_writer_1.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------

separate_no_locations(read_file, write_file_with_locations, write_file_with_no_locations)

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_23.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_24.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_24.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_25.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_26.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_27.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_28.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_29.csv")

# # separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_30.csv",
# #                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_30.csv",
# #                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_30.csv")

# separate_no_locations("../../marawi_tweets_with_location/marawi_tweets_may/official/cleaned_tweets/marawi_tweets_05_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_31.csv")
