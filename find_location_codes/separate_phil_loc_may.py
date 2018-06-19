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

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_june/official/final_tweets/final_tweets/final_tweets/final_tweets/final_tweets/marawi_tweets_06_02.csv"
# file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_june/official/final_tweets/final_tweets/final_tweets/final_tweets/final_tweets/philippines_tweets/marawi_tweets_06_02.csv"
# file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_june/official/final_tweets/final_tweets/final_tweets/final_tweets/final_tweets/other_locations/marawi_tweets_06_02.csv"
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

                    if "'Philippines'" in place or "' Philippines'" in place or "'PHILIPPINES'" in place or "' PHILIPPINES'" in place or "' PH'" in place or "'PH'" in place or "PHILIPPINES" in place:
                        file_writer1.writerow(data)
                        print("***** in the PHILS. | Address : " + str(location))
                    else:
                        if "'CEB'" in place:
                            place = place.replace("'CEB'", "Cebu")
                        elif "'BUDA'" in place:
                            place = place.replace("'BUDA'", "Bukidnon-Davao")
                        elif "MNL" in place:
                            place = place.replace("'MNL'", "Manila")
                        elif "'LB'" in place:
                            place = place.replace("'LB'", "Los Baños")
                        elif "'COMVAL'" in place:
                            place = place.replace("'COMVAL'", "Compostela Valley")
                        elif "'CAR'" in place:
                            place = place.replace("'CAR'", "Cordillera Administrative Region")
                        elif "'CDO'" in place:
                            place = place.replace("'CDO'", "Cagayan de Oro")
                        elif "'LP'" in place:
                            place = place.replace("'LP'", "Las Pinas")
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

                        place = place.upper()

                        if is_in_phil(place):
                            file_writer1.writerow(data)
                            print("***** in the PHILS. | Address : " + str(location))
                        else:
                            file_writer2.writerow(data)
                            print("###### NOPE | Address : " + str(location))
                        
                        # location = geolocator.geocode(place)

                        # print("Address : " + str(location))

                        # if location is not None and "Philippines" in location.address:
                        #     loc = "([" + str(location.address) + "], Location((" + str(location.latitude) + "," + str(location.latitude) + ")))"
                        #     data = [row[0],
                        #             row[1],
                        #             row[2], 
                        #             loc,
                        #             row[4],
                        #             row[5],
                        #             row[6],
                        #             row[7],
                        #             row[8],
                        #             row[9],
                        #             row[10]]
                        #     file_writer1.writerow(data)
                        #     print("***** in the PHILS. | Address : " + str(location))
                        # else:
                       
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
        return geopy.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

#-----------------------------------------------------------------------------------------------------
def is_in_phil(place):
    if "NATIONAL CAPITAL REGION" in place:
        return True
    elif "CORDILLERA ADMINISTRATIVE REGION" in place:
        return True
    elif "ILOCOS" in place:
        return True
    elif "CAGAYAN" in place:
        return True
    elif "LUZON" in place:
        return True
    elif "VISAYAS" in place:
        return True
    elif "MINDANAO" in place:
        return True
    elif "CALABARZON" in place:
        return True
    elif "MIMAROPA" in place:
        return True
    elif "BICOL" in place:
        return True
    elif "ZAMBOANGA" in place:
        return True
    elif "DAVAO" in place:
        return True
    elif "SCCSKARGEN" in place:
        return True
    elif "CARAGA" in place:
        return True
    elif "MOUNTAIN PROVINCE" in place:
        return True
    elif "IFUGAO" in place:
        return True
    elif "BENGUET" in place:
        return True
    elif "ABRA" in place:
        return True
    elif "APAYAO" in place:
        return True
    elif "KALINGA" in place:
        return True
    elif "LA UNION" in place:
        return True
    elif "PANGASINAN" in place:
        return True
    elif "NUEVA VISCAYA" in place:
        return True
    elif "ISABELA" in place:
        return True
    elif "QUIRINO" in place:
        return True
    elif "BATANES" in place:
        return True
    elif "BATAAN" in place:
        return True
    elif "ZAMBALES" in place:
        return True
    elif "TARLAC" in place:
        return True
    elif "PAMPANGA" in place:
        return True
    elif "BULACAN" in place:
        return True
    elif "NUEVA ECIJA" in place:
        return True
    elif "AURORA" in place:
        return True
    elif "RIZAL" in place:
        return True
    elif "CAVITE" in place:
        return True
    elif "LAGUNA" in place:
        return True
    elif "BATANGAS" in place:
        return True
    elif "QUEZON" in place:
        return True
    elif "MINDORO" in place:
        return True
    elif "ROMBLON" in place:
        return True
    elif "PALAWAN" in place:
        return True
    elif "MARINDUQUE" in place:
        return True
    elif "CATANDUANES" in place:
        return True
    elif "CAMARINES" in place:
        return True
    elif "SORSOGON" in place:
        return True
    elif "ALBAY" in place:
        return True
    elif "MASBATE" in place:
        return True
    elif "CAPIZ" in place:
        return True
    elif "AKLAN" in place:
        return True
    elif "ANTIQUE" in place:
        return True
    elif "NEGROS" in place:
        return True
    elif "GUIMARAS" in place:
        return True
    elif "ILOILO" in place:
        return True
    elif "CEBU" in place:
        return True
    elif "BOHOL" in place:
        return True
    elif "SIQUIJOR" in place:
        return True
    elif "LEYTE" in place:
        return True
    elif "SAMAR" in place:
        return True
    elif "BILIRAN" in place:
        return True
    elif "MISAMIS" in place:
        return True
    elif "BUKIDNON" in place:
        return True
    elif "LANAO" in place:
        return True
    elif "CAMIGUIN" in place:
        return True
    elif "COMPOSTELA VALLEY" in place:
        return True
    elif "COTABATO" in place:
        return True
    elif "SULTAN KUDARAT" in place:
        return True
    elif "SARANGANI" in place:
        return True
    elif "AGUSAN" in place:
        return True
    elif "SURIGAO" in place:
        return True
    elif "SIARGAO" in place:
        return True
    elif "DINAGAT" in place:
        return True
    elif "TAWI-TAWI" in place or "TAWITAWI" in place or "TAWI TAWI" in place:
        return True
    elif "BASILAN" in place:
        return True
    elif "SULU" in place:
        return True
    elif "MAGUINDANAO" in place:
        return True
    elif "BUTUAN" in place:
        return True
    elif "CABADBARAN" in place:
        return True
    elif "LEGAZPI" in place:
        return True
    elif "BAYUGAN" in place:
        return True
    elif "LIGAO" in place:
        return True
    elif "TABACO" in place:
        return True
    elif "LAMITAN" in place:
        return True
    elif "BALANGA" in place:
        return True
    elif "LIPA CITY" in place:
        return True
    elif "TANAUAN" in place:
        return True
    elif "BAGUIO" in place:
        return True
    elif "TAGBILARAN" in place:
        return True
    elif "MALAYBALAY" in place:
        return True
    elif "VALENCIA" in place:
        return True
    elif "MALOLOS" in place:
        return True
    elif "MEYCAUAYAN" in place:
        return True
    elif "SAN JOSE DEL MONTE" in place:
        return True
    elif "TUGUEGARAO" in place:
        return True
    elif "IRIGA" in place:
        return True
    elif "NAGA" in place:
        return True
    elif "BACOOR" in place:
        return True
    elif "CAVITE" in place:
        return True
    elif "DASMARIAS" in place:
        return True
    elif "IMUS CITY" in place:
        return True
    elif "TAGAYTAY" in place:
        return True
    elif "TRECE MARTIRES" in place:
        return True
    elif "BOGO" in place:
        return True
    elif "CARCAR" in place:
        return True
    elif "DANAO" in place:
        return True
    elif "LAPU LAPU" in place or "LAPU-LAPU" in place or "LAPULAPU" in place:
        return True
    elif "MANDAUE" in place:
        return True
    elif "TALISAY" in place:
        return True
    elif "TOLEDO" in place:
        return True
    elif "ISABELA" in place:
        return True
    elif "KIDAPAWAN" in place:
        return True
    elif "PANABO" in place:
        return True
    elif "SAMAL" in place:
        return True
    elif "TAGUM" in place:
        return True
    elif "DIGOS" in place:
        return True
    elif "MATI" in place:
        return True
    elif "BORONGON" in place:
        return True
    elif "BATAC" in place:
        return True
    elif "LAOAG" in place:
        return True
    elif "VIGAN" in place:
        return True
    elif "CAUAYAN" in place:
        return True
    elif "PASSI" in place:
        return True
    elif "ILAGAN" in place:
        return True
    elif "TABUK" in place:
        return True
    elif "SAN FERNANDO" in place:
        return True
    elif "CABUYAO" in place:
        return True
    elif "CALAMBA" in place:
        return True
    elif "SAN PABLO" in place:
        return True
    elif "MARAWI" in place:
        return True
    elif "SANTA ROSA" in place:
        return True
    elif "ILIGAN" in place:
        return True
    elif "BAYBAY" in place:
        return True
    elif "ORMOC" in place:
        return True
    elif "TACLOBAN CITY" in place:
        return True
    elif "OROQUIETA" in place:
        return True
    elif "OZAMIS" in place:
        return True
    elif "TANGUB" in place:
        return True
    elif "MANILA" in place:
        return True
    elif "EL SALVADOR" in place:
        return True
    elif "GINGOOG CITY" in place:
        return True
    elif "LAS PINAS" in place:
        return True
    elif "TANGUB" in place:
        return True
    elif "KALIBO" in place:
        return True
    elif "MAKATI" in place:
        return True
    elif "MUNTINLUPA" in place:
        return True
    elif "PARANAQUE" in place:
        return True
    elif "PASAY" in place:
        return True
    elif "MARIKINA" in place:
        return True
    elif "TAGUIG" in place:
        return True
    elif "PASIG" in place:
        return True
    elif "SAN JUAN" in place:
        return True
    elif "CALOOCAN" in place:
        return True
    elif "MALABON" in place:
        return True
    elif "NAVOTAS" in place:
        return True
    elif "BACOLOD" in place:
        return True
    elif "BAGO" in place:
        return True
    elif "CADIZ" in place:
        return True
    elif "ESCALANTE" in place:
        return True
    elif "HIMAMAYLAN" in place:
        return True
    elif "KABANKALAN" in place:
        return True
    elif "LA CARLOTA" in place:
        return True
    elif "SAGAY" in place:
        return True
    elif "SILAY" in place:
        return True
    elif "SIPALAY" in place:
        return True
    elif "BAIS" in place:
        return True
    elif "BAYAWAN" in place:
        return True
    elif "CANLAON" in place:
        return True
    elif "DUMAGUETE" in place:
        return True
    elif "GUIHULNGAN" in place:
        return True
    elif "TANJAY" in place:
        return True
    elif "CABANATUAN" in place:
        return True
    elif "GAPAN" in place:
        return True
    elif "PALAYAN" in place:
        return True
    elif "CALAPAN" in place:
        return True
    elif "PUERTO PRINCESA" in place:
        return True
    elif "ALAMINOS" in place:
        return True
    elif "DAGUPAN" in place:
        return True
    elif "URDANETA" in place:
        return True
    elif "LUCENA" in place:
        return True
    elif "TAYABAS" in place:
        return True
    elif "ANTIPOLO" in place:
        return True
    elif "CALBAYOG" in place:
        return True
    elif "CATBALOGAN" in place:
        return True
    elif "SORSOGON" in place:
        return True
    elif "GENERAL SANTOS CITY" in place:
        return True
    elif "MAASIN" in place:
        return True
    elif "DAPITAN" in place:
        return True
    elif "SAN REMEGIO" in place:
        return True
    elif "TACURONG" in place:
        return True
    elif "TARLAC" in place:
        return True
    elif "PAGADIAN" in place:
        return True
    elif "OLONGAPO" in place:
        return True
    elif "DIPOLOG" in place:
        return True
    elif "PAGA" in place:
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------------------------
csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/all_locations/marawi_tweets_05_23.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_23.csv",
                   "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/marawi_tweets_05_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/other_locations/marawi_tweets_05_31.csv")

