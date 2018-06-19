# -*- coding: utf-8 -*-

import csv
import string

read_path = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_23_raw.csv'
write_path = '../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/with_emotions/marawi_tweets_05_23.csv'

def get_highest_emotions(read_path, write_path):
	with open (write_path, 'wb') as outFile:
		file_writer = csv.writer(outFile)

		with open(read_path,'r') as inFile:
			file_reader = csv.reader(inFile)

			i = 1
			for row in file_reader:
				anger = row[5]
				sadness = row[6]
				joy = row[7]
				fear = row[8]
				disgust = row[9]

				highest_emotion = []
				highest_percent = max(anger, joy, sadness, fear, disgust)

				if highest_percent == anger:
				    highest_emotion.append("anger")
				elif highest_percent == joy:
				    highest_emotion.append("joy")
				elif highest_percent == sadness:
				    highest_emotion.append("sadness")
				elif highest_percent == fear:
				    highest_emotion.append("fear")
				elif highest_percent == disgust:
				    highest_emotion.append("disgust")

				highest_emotion.append(highest_percent) 

				print(i, highest_emotion)
				i = i + 1
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
                        highest_emotion]
				file_writer.writerow(data)



get_highest_emotions(read_path, write_path)