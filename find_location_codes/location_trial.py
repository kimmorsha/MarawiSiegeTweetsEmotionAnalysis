# -*- coding: utf-8 -*-

import csv
import string
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
import sys
geolocator=Nominatim(timeout=5)

reload(sys)
sys.setdefaultencoding('utf-8')

file_to_read = "../marawi_tweets_with_location/marawi_tweets_trial/marawi_tweets_09_04.csv"
file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_trial/philippines_tweets/marawi_tweets_09_04.csv"
file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_trial/other_locations/marawi_tweets_09_04.csv"
# location = "(['MSU', ' Marawi City'], Location((45.6639448, -111.076470877, 0.0)))"
#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:

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
                        row[10]]

                location = row[3]
                print("location : " + str(location))

                if location is not None:
                    index = find_nth(location, "]", 1)
                    place = location[:index]
                    index_2 = find_nth(place, "[", 1)
                    place = place[index_2+1:]
                    place = place.upper()
                    print("place String = " + str(place))

                    # for special cases: ACRONYMS
                    place = place.encode('utf-8')

                    if "'Philippines'" in place:
                        file_writer1.writerow(data)
                        print("***** in the PHILS. | Address : " + str(location))
                    else:
                        if "'CEB'" in place:
                            place = place.replace("'CEB'", "Cebu")
                        elif "'BUDA'" in place:
                            place = place.replace("'BUDA'", "Bukidnon-Davao")
                        elif "'MNL'" in place:
                            place = place.replace("'MNL'", "Manila")
                        elif "'LB'" in place:
                            place = place.replace("'LB'", "Los Baños")
                        elif "'COMVAL'" in place:
                            place = place.replace("'COMVAL'", "Compostela Valley")
                        elif "'CAR'" in place:
                            place = place.replace("'CAR'", "Cordillera Administrative Region")
                        elif "'CDO'" in place:
                            place = place.replace("'CDO'", "Cagayan de Oro")
                        elif "'CAR'" in place:
                            place = place.replace("'CAR'", "Cordillera Administrative Region")
                        elif "'LP'" in place:
                            place = place.replace("'LP'", "Las Piñas")
                        elif "'NCR'" in place:
                            place = place.replace("'NCR'", "National Capital Region")
                        elif "'BCD'" in place:
                            place = place.replace("'BCD'", "Bacolod")
                        elif "'DGT'" in place:
                            place = place.replace("'DGT'", "Dumaguete")
                        elif "'DVO'" in place:
                            place = place.replace("'DVO'", "Davao")
                        elif "'ILO'" in place:
                            place = place.replace("'ILO'", "Iloilo")
                        elif "'KLO'" in place:
                            place = place.replace("'KLO'", "Kalibo, Aklan")
                        elif "'LP'" in place:
                            place = place.replace("'LP'", "Las Piñas")
                        elif "'NEGOCC'" in place:
                            place = place.replace("'NEGOCC'", "Negros Occidental")
                        elif "'NEGOR'" in place:
                            place = place.replace("'NEGOR'", "Negros Oriental")
                        elif "'QC'" in place:
                            place = place.replace("'QC'", "Quezon City")
                        elif "'GENSAN'" in place:
                            place = place.replace("'GENSAN'", "General Santos")
                        elif "'GES'" in place:
                            place = place.replace("'GES'", "General Santos")
                        elif "'ZC'" in place:
                            place = place.replace("'ZC'", "Zamboanga City")
                        elif "'ZAM'" in place:
                            place = place.replace("'ZAM'", "Zamboanga City")
                        elif "'NRA'" in place:
                            place = place.replace("'NRA'", "''")


                        location = do_geocode(place)

                        print("Address : " + str(location))

                        if location is not None and "Philippines" in location.address:
                            loc = "([" + str(location.address) + "], Location((" + str(location.latitude) + "," + str(location.latitude) + ")))"
                            data = [row[0],
                                    row[1],
                                    row[2], 
                                    loc,
                                    row[4],
                                    row[5],
                                    row[6],
                                    row[7],
                                    row[8],
                                    row[9],
                                    row[10]]
                            file_writer1.writerow(data)
                            print("***** in the PHILS. | Address : " + str(location))
                        else:
                            file_writer2.writerow(data)
                            print("###### NOPE | Address : " + str(location))
                else:
                    file_writer2.writerow(data)
                    print("###### NOPE | Address : " + str(location))

#-----------------------------------------------------------------------------------------------------
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#-----------------------------------------------------------------------------------------------------
def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

#-----------------------------------------------------------------------------------------------------

csv_read_and_write(file_to_read,
                    file_to_write1,
                    file_to_write2)







# # -*- coding: utf-8 -*-

# import csv
# import string
# from geopy.geocoders import Nominatim
# geolocator = Nominatim()
# from geopy.exc import GeocoderTimedOut
# import unicodedata
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

# # file_to_read = "../marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_03.csv"
# # file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_septembertweets/marawi_tweets_09_03.csv"
# # file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_septemberons/marawi_tweets_09_03.csv"
# location = "(['NegOcc'])"
# #------------------------------------------------------------------------------------------------------
# def csv_read_and_write(loc):
#     # with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
#     #     file_writer1 = csv.writer(outFile1)
#     #     file_writer2 = csv.writer(outFile2)

#     #     with open(read_path,'r') as inFile:
#     #         fileReader = csv.reader(inFile)
#     #         for row in fileReader:
#     #             loc = row[5]
#     #             print("location : " + str(loc))

#                 # loc = unicodedata.normalize("NFKD", loc)
#                 location = get_location(loc)
#                 print("Address : " + str(location.address))
#                 print("Latitude : " + str(location.latitude))
#                 print("Longitude : " + str(location.longitude))

#                 # data = [row[0],
#                 #         row[1],
#                 #         row[2],
#                 #         row[3],
#                 #         row[4],
#                 #         row[5],
#                 #         row[6],
#                 #         row[7],
#                 #         row[8],
#                 #         row[9],
#                 #         row[10]]

#                 '''
#                 Keywords:
#                     'PH' 
#                     'philippines' 
#                     'Republic of the Philippines'
#                     ''
#                 '''

#                 # if phil_loc is True:
#                 # 	file_writer1.writerow(data)
#                 # else:
#                 # 	file_writer2.writerow(data)
# #-----------------------------------------------------------------------------------------------------
# def get_location(location):

#     if location is not None:
#         index = find_nth(location, "]", 1)
#         print("Index of Last Bracket of Place = " + str(index))
#         # length = len(location) + 1
#         place = location[:index]
#         print("Place String = " + str(place))

#         index_2 = find_nth(place, "[", 1)
#         print("index of [ = " + str(index_2)) 
#         place = place[index_2+1:]
#         print("place String = " + str(place))

#         # for special cases: ACRONYMS

#         # if "'CEB'" in place:
#         #     place = place.replace("'CEB'", "Cebu")
#         # elif "'CDO'" in place:
#         #     place = place.replace("'CDO'", "Cagadayan De Oro")
#         # elif "'ARMM'" in place:
#         #     place = place.replace("'CDO'", "Cagadayan De Oro")


#         location = geolocator.geocode(place)

#         return location
#     else:
#         return None

# #-----------------------------------------------------------------------------------------------------
# def is_philippines(address):
#     address = address.lower()
#     return "philippines" in address
        
# #-----------------------------------------------------------------------------------------------------
# def find_nth(haystack, needle, n):
#     start = haystack.find(needle)
#     while start >= 0 and n > 1:
#         start = haystack.find(needle, start+len(needle))
#         n -= 1
#     return start

# #-----------------------------------------------------------------------------------------------------

# csv_read_and_write(location)