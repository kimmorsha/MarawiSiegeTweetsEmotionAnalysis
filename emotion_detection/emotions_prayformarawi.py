# -*- coding: utf-8 -*-

import csv
import string
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions


readFile = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_23.csv'
writeFile = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_23.csv'
#------------------------------------------------------------------------------------------------------
def analyze_emotions(read_path, write_path):
	# natural_language_understanding = NaturalLanguageUnderstandingV1(
	# 	username='1572033b-4578-4a47-9a78-de682f345725',
	# 	password='NfHpqieFiUYD',
	# 	version='2018-03-16')

	# response = natural_language_understanding.analyze(
	# 		    	language="en",
	# 		    	text="Pray for Marawi",
	# 		    	features=Features(emotion=EmotionOptions()))

	# jsonData = json.dumps(response, indent=2)
	# print(jsonData)
	# my_dict = json.loads(jsonData)
	# my_dict2 = my_dict["emotion"]
	# document = my_dict2["document"]
	# emotion = document["emotion"]

	# highest_emotion = get_highest_emotion(emotion["anger"],emotion["joy"],emotion["sadness"],emotion["fear"],emotion["disgust"])

	# print(highest_emotion)
	anger = 0.035032
	joy = 0.028972
	sadness = 0.4138
	fear = 0.584248
	disgust = 0.158603
	highest_emotion = ['fear', 0.584248]

	with open (write_path, 'wb') as outFile:
		file_writer = csv.writer(outFile)

		i = 1
		with open(read_path,'r') as inFile:
			fileReader = csv.reader(inFile)
			for row in fileReader:
				tweet = row[4]
				print(i, tweet)

				data = [row[0],
						row[1],
						"#PrayForMarawi",
						row[5],
						"en",
						anger,
						joy,
						sadness,
						fear,
						disgust,
						highest_emotion]

				file_writer.writerow(data)
				i = i+1

#-----------------------------------------------------------------------------------------------------
analyze_emotions(readFile, writeFile)

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_24.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_24.csv')

analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_25.csv',
				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_25.csv')

analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_26.csv',
				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_26.csv')

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_27.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_27.csv')

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_28.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_28.csv')

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_29.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_29.csv')

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_30.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_30.csv')

# analyze_emotions('../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/marawi_tweets_05_31.csv',
# 				 '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_31.csv')

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_01.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_01.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_02.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_03.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_03.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_04.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_04.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_05.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_05.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_06.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_06.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_07.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_08.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_09.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_10.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_11.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_11.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_12.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_12.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_13.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_13.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_14.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_14.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_15.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_15.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_16.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_16.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_17.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_17.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_18.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_18.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_19.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_19.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_20.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_20.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_21.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_21.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_22.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_23.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_23.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_24.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_24.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_25.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_25.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_26.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_26.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_27.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_27.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_28.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_28.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_29.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_29.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/marawi_tweets_06_30.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/with_emotions/marawi_tweets_06_30.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_01.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_01.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_02.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_03.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_03.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_04.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_04.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_05.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_05.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_06.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_06.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_07.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_08.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_09.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_10.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_11.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_11.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_12.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_12.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_13.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_13.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_14.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_14.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_15.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_15.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_16.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_16.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_17.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_17.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_18.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_18.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_19.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_19.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_20.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_20.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_21.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_21.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_22.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_23.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_23.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_24.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_24.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_25.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_25.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_26.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_26.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_27.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_27.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_28.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_28.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_29.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_29.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_30.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_30.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/marawi_tweets_07_31.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/with_emotions/marawi_tweets_07_31.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_01.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_01.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_02.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_03.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_03.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_04.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_04.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_05.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_05.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_06.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_06.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_07.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_08.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_09.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_10.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_11.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_11.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_12.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_12.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_13.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_13.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_14.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_14.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_15.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_15.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_16.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_16.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_17.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_17.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_18.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_18.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_19.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_19.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_20.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_20.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_21.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_21.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_22.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_23.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_23.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_24.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_24.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_25.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_25.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_26.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_26.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_27.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_27.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_28.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_28.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_29.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_29.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_30.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_30.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/marawi_tweets_08_31.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/with_emotions/marawi_tweets_08_31.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_01.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_01.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_02.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_03.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_03.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_04.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_04.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_05.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_05.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_06.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_06.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_07.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_08.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_09.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_10.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_11.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_11.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_12.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_12.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_13.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_13.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_14.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_14.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_15.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_15.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_16.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_16.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_17.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_17.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_18.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_18.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_19.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_19.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_20.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_20.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_21.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_21.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_22.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_23.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_23.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_24.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_24.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_25.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_25.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_26.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_26.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_27.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_27.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_28.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_28.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_29.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_29.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/marawi_tweets_09_30.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/with_emotions/marawi_tweets_09_30.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_01.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_01.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_02.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_03.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_03.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_04.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_04.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_05.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_05.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_06.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_06.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_07.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_08.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_09.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_10.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_11.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_11.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_12.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_12.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_13.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_13.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_14.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_14.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_15.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_15.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_16.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_16.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_17.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_17.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_18.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_18.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_19.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_19.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_20.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_20.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_21.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_21.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_22.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/marawi_tweets_10_23.csv",
#                  "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/with_emotions/marawi_tweets_10_23.csv")
