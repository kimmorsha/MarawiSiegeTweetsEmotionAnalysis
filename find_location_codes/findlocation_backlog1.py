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

# BACKLOG 1

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_22_1.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_05_22_1.csv')

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_23.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_05_23.csv')

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_24_2.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_05_24_2.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_22_to_05_24.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_05_22_to_05_24.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_28_to_05_29.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_05_28_to_05_29.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_31_to_06_01.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_05_31_to_06_01.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_11_to_06_12.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_06_11_to_06_12.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_24_to_06_25.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_06_24_to_06_25.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_27_to_06_28.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_06_27_to_06_28.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_07_03_to_07_04.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_07_03_to_07_04.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_07_08_to_07_09.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_07_08_to_07_09.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_07_09_to_07_11.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_07_09_to_07_11.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_07_23_to_07_24.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_07_23_to_07_24.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_08_05_to_08_07.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_08_05_to_08_07.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_08_13_to_08_14.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_08_13_to_08_14.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_08_23_to_08_25.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_08_23_to_08_25.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_08_31_to_09_01.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_08_31_to_09_01.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_05_to_09_10.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_05_to_09_10.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_04_to_09_05.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_04_to_09_05.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_05_to_09_06.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_05_to_09_06.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_06_to_09_07.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_06_to_09_07.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_07_to_09_08.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_07_to_09_08.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_08_to_09_09.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_08_to_09_09.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_09_to_09_10.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_09_to_09_10.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_10_to_09_11.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_10_to_09_11.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_15_to_09_17.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_15_to_09_17.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_17_to_09_18.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_17_to_09_18.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_09_30_to_10_01.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_09_30_to_10_01.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_10_04_to_10_05.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_10_04_to_10_05.csv')

# csv_read_and_write('../to_be_skimbordeng/marawi_tweets_10_21_to_10_24.csv', 
#                     '../to_be_skimbordeng/with_locations/marawi_tweets_10_21_to_10_24.csv')
