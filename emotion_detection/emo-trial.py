# -*- coding: utf-8 -*-

import csv
import string
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions

#------------------------------------------------------------------------------------------------------
# def analyze_emotions(tweet):
# 	natural_language_understanding = NaturalLanguageUnderstandingV1(
# 		username='ab458f9c-8b2e-4688-9ec0-ce7810b6f997',
# 		password='Mnh5qTNFYrNN',
# 		version='2018-03-16')

# 	print(tweet)

# 	if tweet is not None:
# 		response = natural_language_understanding.analyze(
# 			text=tweet,
# 			features=Features(emotion=EmotionOptions()))

# 		jsonData = json.dumps(response, indent=2)
# 		print(jsonData)
# 		my_dict = json.loads(jsonData)
# 		my_dict2 = my_dict["emotion"]
# 		my_dict3 = my_dict2["document"]
# 		my_dict4 = my_dict3["emotion"]
# 		print(my_dict4["anger"])
# 		print(my_dict4["joy"])
# 		print(my_dict4["sadness"])
# 		print(my_dict4["fear"])
# 		print(my_dict4["disgust"])

# 		highest_emotion = get_highest_emotion(my_dict4["anger"],
# 						            		my_dict4["joy"],
# 						            		my_dict4["sadness"],
# 						            		my_dict4["fear"],
		# 				            		my_dict4["disgust"])

		# print(highest_emotion)

# #-----------------------------------------------------------------------------------------------------
# def get_highest_emotion(anger, joy, sadness, fear, disgust):
# 	return max(anger, joy, sadness, fear, disgust)

#-----------------------------------------------------------------------------------------------------
def remove_words_with_numbers(tweet):
	t = ""
	for word in tweet.split():
		print(word)
		if num_there(word) is False:
			t = t + word
			t += " "
	return t


def num_there(s):
    return any(i.isdigit() for i in s)

print(remove_words_with_numbers("pray u8 for marawi"))