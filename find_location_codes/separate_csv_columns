# -*- coding: utf-8 -*

import csv
import string

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