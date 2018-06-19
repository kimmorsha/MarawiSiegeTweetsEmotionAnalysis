import os

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

path =  os.getcwd()
filenames = os.listdir(path)

print(path)
num = 8

for filename in filenames:
	print(filename)
	if f
	if num < 9:
		num = num + 1
		new_filename = "marawi_tweets_08_0" + str(num) + ".csv"
		os.rename(filename, new_filename)
	elif num == 13 or num == 14 or num == 23 or num == 24 or num == 25 or num == 26:
		pass
	else:
		num = num + 1
		new_filename = "marawi_tweets_08_" + str(num) + ".csv"
		os.rename(filename, new_filename)
	
