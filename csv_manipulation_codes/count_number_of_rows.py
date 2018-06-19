# -*- coding: utf-8 -*-

import csv
import string
import pandas as pd

def count_number_of_rows(filename):
	sum = 0
	with open(filename,'r') as inFile:
	    file_reader = csv.reader(inFile)

	    for row in file_reader:
	        sum += 1
	return sum

def get_count_for_may():
	count = 0
	
	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_24.csv")
	
	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_25.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_26.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_27.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_28.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_29.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_30.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_may/official/all_tweets/marawi_tweets_05_31.csv")

	print count

def get_count_for_june():
	count = 0

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_01.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_02.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_03.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_04.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_05.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_06.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_07.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_08.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_09.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_10.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_11.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_12.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_13.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_14.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_15.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_16.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_17.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_18.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_19.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_20.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_21.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_22.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_23.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_24.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_25.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_26.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_27.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_28.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_29.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_30.csv")

	print count

def get_count_for_july():
	count = 0

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_01.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_02.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_03.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_04.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_05.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_06.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_07.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_08.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_09.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_10.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_11.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_12.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_13.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_14.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_15.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_16.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_17.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_18.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_19.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_20.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_21.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_22.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_23.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_24.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_25.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_26.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_27.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_28.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_29.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_30.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_july/official/all_tweets/marawi_tweets_07_31.csv")

	print count

def get_count_for_aug():
	count = 0

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_01.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_02.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_03.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_04.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_05.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_06.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_07.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_08.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_09.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_10.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_11.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_12.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_13.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_14.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_15.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_16.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_17.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_18.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_19.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_20.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_21.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_22.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_23.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_24.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_25.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_26.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_27.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_28.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_29.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_30.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_august/official/all_tweets/marawi_tweets_08_31.csv")

	print count

def get_count_for_sept():
	count = 0
		
	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_01.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_02.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_03.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_04.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_05.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_06.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_07.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_08.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_09.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_10.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_11.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_12.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_13.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_14.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_15.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_16.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_17.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_18.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_19.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_20.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_21.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_22.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_23.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_24.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_25.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_26.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_27.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_28.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_29.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_september/official/all_tweets/marawi_tweets_09_30.csv")

	print count

def get_count_for_oct():
	count = 0

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_01.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_02.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_03.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_04.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_05.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_06.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_07.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_08.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_09.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_10.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_11.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_12.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_13.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_14.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_15.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_16.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_17.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_18.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_19.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_20.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_21.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_22.csv")

	count += count_number_of_rows("../marawi_tweets_with_location/marawi_tweets_october/official/all_tweets/marawi_tweets_10_23.csv")

	print count

# get_count_for_may()
# get_count_for_june()
# get_count_for_july()
# get_count_for_aug()
# get_count_for_sept()
# get_count_for_oct()


