 # -*- coding: utf-8 -*-

import csv
import string
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

validchars = string.ascii_letters + string.digits + ' '

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open(write_path, 'wb') as outFile1:
        file_writer1 = csv.writer(outFile1)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = str(row[4])
                tweet = tweet.decode('utf-8', 'replace')
                tweet = remove_punctuations(tweet)
                print(tweet)
                    
                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        tweet,
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9]]

                file_writer1.writerow(data)

                i = i + 1
#-----------------------------------------------------------------------------------------------------
def remove_punctuations(s):
    clean = ''.join(c for c in s if c in validchars)
    return clean

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_23.csv")

    # csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_24.csv",
    #                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_24.csv")
        
# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_25.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_26.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_27.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_27.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_28.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_30.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_may/official/english_tweets/marawi_tweets_05_31.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_may/official/no_stopwords_punc/marawi_tweets_05_31.csv")
