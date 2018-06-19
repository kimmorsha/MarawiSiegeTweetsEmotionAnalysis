# -*- coding: utf-8 -*-

import csv
import urllib
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
URL_INIT = 'https://twitter.com/'

file_to_read = "./marawi_tweets_raw/marawi_tweets_may/marawi_tweets_05_23_to_05_24.csv"
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
            fileReader = csv.DictReader(inFile, delimiter=';')
            for row in fileReader:
                username = row["username"]
                print("username = " + username)
                location = findLocation(username)
                if location is None:
                    data = [row["username"],
                            row["date"],
                            row["retweets"],
                            row["favorites"],
                            row["text"],
                            row["geo"],
                            row["mentions"],
                            row["hashtags"],
                            row["id"],
                            row["permalink"]]
                else:
                    data = [row["username"],
                            row["date"],
                            row["retweets"],
                            row["favorites"],
                            row["text"],
                            location,
                            row["mentions"],
                            row["hashtags"],
                            row["id"],
                            row["permalink"]]
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
JUNE
'''
# csv_read_and_write('./marawi_tweets_june/marawi_tweets_06_01_to_06_02.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_01_to_06_02.csv')
# csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/marawi_tweets_06_02_to_06_03.csv', 
#                     './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_02_to_06_03.csv')
csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_01_to_06_02.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_01_to_06_02.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_04_to_06_05.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_04_to_06_05.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_05_to_06_06.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_05_to_06_06.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_06_to_06_07.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_06_to_06_07.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_07_to_06_08.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_07_to_06_08.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_08_to_06_09.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_08_to_06_09.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_09_to_06_10.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_09_to_06_10.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_10_to_06_11.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_10_to_06_11.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_12_to_06_13.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_12_to_06_13.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_12.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_12.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_13_to_06_14.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_13_to_06_14.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_14_to_06_15.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_14_to_06_15.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_15_to_06_16.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_15_to_06_16.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_16_to_06_17.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_16_to_06_17.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_17_to_06_18.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_17_to_06_18.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_18_to_06_19.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_18_to_06_19.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_19_to_06_20.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_19_to_06_20.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_20_to_06_21.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_20_to_06_21.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_21_to_06_22.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_21_to_06_22.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_22_to_06_23.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_22_to_06_23.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_23_to_06_24.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_23_to_06_24.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_24_to_06_25.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_24_to_06_25.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_25_to_06_26.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_25_to_06_26.csv')

csv_read_and_write('./marawi_tweets_raw/marawi_tweets_june/no_locations_yet/marawi_tweets_06_26_to_06_27.csv', 
                    './marawi_tweets_with_location/marawi_tweets_june/marawi_tweets_06_26_to_06_27.csv')








