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
csv_read_and_write('../to_be_skimbordeng/marawi_tweets_05_31_to_06_01.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_05_31_to_06_01.csv')

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_11_to_06_12.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_06_11_to_06_12.csv')

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_24_to_06_25.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_06_24_to_06_25.csv')

csv_read_and_write('../to_be_skimbordeng/marawi_tweets_06_27_to_06_28.csv', 
                    '../to_be_skimbordeng/with_locations/marawi_tweets_06_27_to_06_28.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_09_to_08_13.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_09_to_08_13.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_14_to_08_16.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_14_to_08_16.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_16_to_08_17.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_16_to_08_17.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_17_to_08_20.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_17_to_08_20.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_20_to_08_21.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_20_to_08_21.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_21_to_08_22.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_21_to_08_22.csv')

# csv_read_and_write('./marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_22_to_08_23.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_22_to_08_23.csv')

# csv_read_and_write('./marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_25_to_08_27_discontinued.csv', 
#                     './marawi_tweets_with_location2/marawi_tweets_august/marawi_tweets_08_25_to_08_27.csv')
