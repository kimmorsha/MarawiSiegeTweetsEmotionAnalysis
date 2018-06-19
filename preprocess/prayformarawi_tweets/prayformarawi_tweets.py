# -*- coding: utf-8 -*-

import csv
import string
import preprocessor as p

read_file = "../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_24.csv"
write_file = "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_24.csv"

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

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/non_english_tweets/marawi_tweets_05_23.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_24.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_24.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_25.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_25.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_26.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_29.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_31.csv")
