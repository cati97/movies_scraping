# [] read data from csv file
# [] change data into a dictionary
# [] save this dictionary into json file

import json


with open("csv_file.txt", "r") as csv:  # the same as - csv = open("csv_file.txt", "r") and csv.close() later
    lines = csv.readlines()

# closes the file automatically for us!

lines = [line.strip() for line in lines[1:]]

list_of_dicts = []  # we can append to it some dictionaries

for line in lines:
    info_as_list = line.split(",")
    club, city, country = info_as_list
    list_of_dicts.append({"club": club, "city": city, "country": country})


with open("json_file.txt", "w") as json_file:
    json.dump(list_of_dicts, json_file)

json_file.close()
