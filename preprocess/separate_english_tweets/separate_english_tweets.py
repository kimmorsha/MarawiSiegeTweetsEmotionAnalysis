# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string
import preprocessor as p

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_1.csv"
# file_of_english_tweets = "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_1.csv"
# file_of_non_english_tweets = "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_1.csv"

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
                cleaned_tweet = p.clean(tweet)
                cleaned_tweet = unicode(cleaned_tweet, 'utf-8')
                is_english = detect_language(cleaned_tweet) # where we call the function that detects if it is english or not
                print(is_english)
                
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

                if is_english is True:
                    file_writer1.writerow(data)
                else:
                    file_writer2.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------
def detect_language(tweet):
	# tweet = filter(lambda x: x in string.printable, tweet)
	# is_utf8 = isUTF8Strict(tweet) 
	# if is_utf8:
		# tweet = tweet.decode('utf-8')
    try:
        print(tweet)
        languages = Detector(tweet, quiet = True).languages
        is_english = False
        max_confidence = 0

        for language in languages:
            if language.name == "English":
                max_confidence = language.confidence
                print(language.confidence)
                if float(language.confidence) >= 93.0:
                   is_english = True
                else:
                    is_english = False
            else:
                if float(language.confidence) >= 10.0:
                    is_english = False
        return is_english
    except UnicodeDecodeError:
        print("UnicodeDecodeError ew")
        return False
	# else:
	# 	return False

#------------------------------------------------------------------------------------------------------
LATIN_1_CHARS = (
    ('\xe2\x80\x99', "'"),
    ('\xc3\xa9', 'e'),
    ('\xc2\xa0', ' '),
    ('\xe2\x80\x90', '-'),
    ('\xe2\x80\x91', '-'),
    ('\xe2\x80\x92', '-'),
    ('\xe2\x80\x93', '-'),
    ('\xe2\x80\x94', '-'),
    ('\xe2\x80\x94', '-'),
    ('\xe2\x80\x98', "'"),
    ('\xe2\x80\x9b', "'"),
    ('\xe2\x80\x9c', '"'),
    ('\xe2\x80\x9c', '"'),
    ('\xe2\x80\x9d', '"'),
    ('\xe2\x80\x9e', '"'),
    ('\xe2\x80\x9f', '"'),
    ('\xe2\x80\xa6', '...'),
    ('\xe2\x80\xb2', "'"),
    ('\xe2\x80\xb3', "'"),
    ('\xe2\x80\xb4', "'"),
    ('\xe2\x80\xb5', "'"),
    ('\xe2\x80\xb6', "'"),
    ('\xe2\x80\xb7', "'"),
    ('\xe2\x81\xba', "+"),
    ('\xe2\x81\xbb', "-"),
    ('\xe2\x81\xbc', "="),
    ('\xe2\x81\xbd', "("),
    ('\xe2\x81\xbe', ")")
)


def clean_latin1(data):
    try:
        return data.encode('utf-8')
    except UnicodeDecodeError:
        data = data.decode('iso-8859-1')
        for _hex, _char in LATIN_1_CHARS:
            data = data.replace(_hex, _char)
        return data.encode('utf8')

#--------------------------------------------------------------------------------------------------------

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_01.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_02.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_03.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_04.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_05.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_06.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_07.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_08.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_09.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_10.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_11.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_12.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_13.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_14.csv",
                   # "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_14.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_15.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_16.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_17.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_18.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_19.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_20.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_21.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_22.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_25.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_26.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_27.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_28.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_29.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/english_tweets/marawi_tweets_08_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/non_english_tweets/marawi_tweets_08_31.csv")
