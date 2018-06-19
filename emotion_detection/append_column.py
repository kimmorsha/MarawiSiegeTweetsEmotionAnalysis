# -*- coding: utf-8 -*-

import csv
import string
import pandas as pd

# read_file = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_23.csv'
# write_file = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/all_locations/marawi_tweets_05_23.csv'

read_file = './marawi_tweets_05_23.csv'
write_file = './here/marawi_tweets_05_23.csv'

with open(read_file,'r') as csvinput:
    with open(write_file, 'w') as csvoutput:
        writer = csv.writer(csvoutput)

        for row in csv.reader(csvinput):
            writer.writerow(row+[10])