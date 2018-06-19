 # -*- coding: utf-8 -*-

import csv
import string
import re
import io
import itertools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words('english'))
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
                # tweet = split_words(tweet)
                tweet = tweet.lower()
                tweet = has_prayformarawi(tweet)
                tweet = improve_repeated(tweet)

                print(tweet)
                # word_tokens = word_tokenize(tweet)
                # filtered_sentence = [w for w in word_tokens if not w in stop_words]
                # filtered_sentence = []

                # for w in word_tokens:
                #     if w not in stop_words:
                #         filtered_sentence.append(w)

                # cleaned_sentence = []

                # for w in filtered_sentence:
                #     w = str(w)
                #     cleaned_sentence.append(w)

                # print(cleaned_sentence)

                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        tweet, # cleaned_sentence,
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10]]

                file_writer1.writerow(data)

                i = i + 1
#-----------------------------------------------------------------------------------------------------
def remove_punctuations(s):
    clean = ''.join(c for c in s if c in validchars)
    return clean

def improve_repeated(text):
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    return text 

def remove_url(text):
    mypatt = "http[s]?://[a-zA-Z0-9]*"
    strongpatt = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(strongpatt, text)
    f = 0
    for url in urls:
        i = text.index(url)
        text = text[:i] + text[i+len(url):]
    return text

def split_words(text):
    ans = ""
    for a in re.findall('[A-Z][^A-Z]*', text):
        ans+=a.strip()+' '
    return ans

def has_prayformarawi(tweet):
    return tweet.replace("prayformarawi", "pray for marawi")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_01.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_01.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_02.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_02.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_03.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_03.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_04.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_04.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_05.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_05.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_06.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_06.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_07.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_07.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_08.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_08.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_09.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_09.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_10.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_10.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_11.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_11.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_12.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_12.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_13.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_13.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_14.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_14.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_15.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_15.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_16.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_16.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_17.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_17.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_18.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_18.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_19.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_19.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_20.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_20.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_21.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_21.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_22.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_22.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_23.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_23.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_24.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_24.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_25.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_25.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_26.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_26.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_27.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_27.csv")

csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_28.csv",
                   "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_28.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_29.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_29.csv")

# csv_read_and_write("../../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_30.csv",
#                    "../../marawi_tweets_with_location/marawi_tweets_june/official/cleaned_tweets/marawi_tweets_06_30.csv")