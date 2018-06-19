# -*- coding: utf-8 -*-

import csv
import urllib
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
URL_INIT = 'https://twitter.com/'

file_to_read = "./marawi_tweets_may/marawi_tweets_05_23_to_05_24.csv"
file_to_write = "./marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_23_to_05_24.csv"

#The located userlocations are appended to this list
list_of_found_userlocations = []

#The not located userlocations are appended to this list. 
#Maybe they contain some typo or something else like that. 
list_of_nonfound_userlocations = []
#--------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open(write_path ,'w') as outFile:
        fileWriter = csv.writer(outFile)
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                original_location = row[5]
                print("original_location = " + original_location)
                if original_location is not "":
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
                    fileWriter.writerow(data)
                else:
                    username = row[0]
                    print("username = " + username)
                    location = findLocation(username)
                    if location is None:
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
                    else:
                        data = [row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                                location,
                                row[6],
                                row[7],
                                row[8],
                                row[9]]
                    fileWriter.writerow(data)
                

#----------------------------------------------------------------------
def parse_url(tweet_user):
    url = URL_INIT+ tweet_user.strip('@')
    return url


def findLocation(user):
    try:
        url = parse_url(user)
        print("url is + " + url)
        response = urllib.urlopen(url)
    except:
        print("error in opening the url")
        return

    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    try:
        location = soup.find('span','ProfileHeaderCard-locationText').text.encode('utf8').strip('\n').strip()
        if location is not None:
            print("\tlocation is found = " + location)
            if ',' in location:
                splitted_location = location.split(',')
            else:
                splitted_location = re.split('|;|-|/|°|#', location)
            try:
                print(splitted_location)
                if splitted_location:
                    located_location = geolocator.geocode(splitted_location[0], timeout=100)
                else:
                    located_location = geolocator.geocode(location, timeout=100)
                if located_location:
                    if splitted_location:
                        user_plus_location = (splitted_location, located_location)
                    else:
                        user_plus_location = (location, located_location)
                    list_of_found_userlocations.append(user_plus_location)
                    print(user_plus_location)
                    return user_plus_location
                else:
                    user_plus_incorrect_location = (user, location)
                    list_of_nonfound_userlocations.append(user_plus_incorrect_location)
                    return ""
            except GeocoderTimedOut as e:
                print("Error: geocode failed on input %s with message %s"%(location, e))
    except:
        return ""
#------------------------------------------------------------------------------
'''
JULY
'''

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_06_28_to_07_02.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_06_28_to_07_02.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_02_to_07_03.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_02_to_07_03.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_04_to_07_05.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_04_to_07_05.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_04.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_july/official/marawi_tweets_07_04.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_05.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_july/official/marawi_tweets_07_05.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_06.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_july/official/marawi_tweets_07_06.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_07.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_july/official/marawi_tweets_07_07.csv')

csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_08.csv', 
                    './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_08.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_09_to_07_10.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_09_to_07_10.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_10_to_07_11.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_10_to_07_11.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_11_to_07_12.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_11_to_07_12.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_12_to_07_13.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_12_to_07_13.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_13_to_07_14.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_13_to_07_14.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_14_to_07_15.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_14_to_07_15.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_15_to_07_21.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_15_to_07_21.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_21_to_07_23.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_21_to_07_23.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_july/marawi_tweets_07_24_to_08_02.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_july/marawi_tweets_07_24_to_08_02.csv')