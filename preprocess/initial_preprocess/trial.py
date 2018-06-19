# -*- coding: utf-8 -*-

import csv
import string
import preprocessor as p

tweet = '#PrayForMarawi'

#------------------------------------------------------------------------------------------------------
def trial(tweet):
	print(tweet)
	p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
	cleaned_tweet = p.clean(tweet)
	print(cleaned_tweet)

#-----------------------------------------------------------------------------------------------------
trial(tweet)
