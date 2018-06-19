# -*- coding: utf-8 -*-

import csv
import string
import preprocessor as p

# read_file = "../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_24.csv"
# write_file = "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_24.csv"

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open (write_path, 'wb') as outFile:
        file_writer = csv.writer(outFile)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                print("raw tweet : " + tweet)
                
                decode = decode_tweet(tweet)
                if decode is not None:
                	tweet = decode

	                p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.EMOJI)
	                tweet = p.clean(tweet)
	                print("semi-cleaned tweet : " + tweet)
	                
	                verdict = is_prayformarawi_tweet(tweet)
	                print(verdict)
	                
	                data = [row[0],
	                        row[1],
	                        row[2],
	                        row[3],
	                        row[4],
	                        row[5],
	                        row[6],
	                        row[7],
	                        row[8],
	                        row[9]]

	                if verdict is True:
	                    file_writer.writerow(data)
	                    i = i + 1
             	
             	print("#prayformarawi tweets count: ", i)

#-----------------------------------------------------------------------------------------------------
def is_prayformarawi_tweet(tweet):
	try:
		tweet = tweet.upper()

		if tweet == "#PRAYFORMARAWI" or tweet == "# PRAYFORMARAWI":
			return True
		else:
			return False

	except UnicodeDecodeError:
		print("UnicodeDecodeError ew")
		return False
#-----------------------------------------------------------------------------------------------------
def decode_tweet(tweet):
	try:
		return tweet.encode("utf8")
	except UnicodeDecodeError:
		print("UnicodeDecodeError ew")
		return None
#-----------------------------------------------------------------------------------------------------

#csv_read_and_write(read_file, write_file)

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_01.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_04.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_05.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_05.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_06.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_06.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_07.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_07.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_08.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_09.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_10.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_11.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_12.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_13.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_13.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_14.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_14.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_15.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_16.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_21.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_22.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_23.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_23.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_24.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_30.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_31.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_31.csv")
