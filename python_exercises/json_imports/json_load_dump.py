import json

# convert a json file into dictionary
file_pointer = open("food.txt", "r")
file_content_as_dict = json.load(file_pointer)  # returns a dictionary
file_pointer.close()

print(file_content_as_dict["food"][0]['type'])

# convert a dictionary/list into json file

cars = {"cars": [
    {"color": "black", "production_year": 2018},
    {"color": "white", "production_year": 2000},
]}

cars_file = open("cars.txt", "w")
json.dump(cars, cars_file)  # first arg - dictionary or list, second - file where to save
cars_file.close()

# convert json string into dictionary

my_json_string = '[{"color": "black", "production_year": 2018}]'

string_as_dict = json.loads(my_json_string)

print(string_as_dict[0])


