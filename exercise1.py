## fetch data from API call using Requests module from https://api.postcodes.io/postcodes/se120nb
## display key:value pairs with in dictionaries
# iterate through nested dictionaries and display outcome
## create a function to return the above values (key:value)
## create a class and move the code block inside the class

# importing requests
# importing json

import requests

import json

with open("counties.json") as counties:
    data = json.load(counties)

class JSONReader:
    def get_all_values(self, nested_dictionary):  # This is a method
        for key, value in nested_dictionary.items():  # iterate through the key, value pairs in this dictionary
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value)  # recall this method passing in that dictionary to iterate through it
        else:
            print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through

json_reader = JSONReader()  # Create instance of this function

json_reader.get_all_values(data)  # Returns all the values inside a dictionary including any nested dictionaries