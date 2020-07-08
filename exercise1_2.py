# importing request and json
import requests

import json

# collecting the site content
# loading the data

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb").content

# new object called data which will store json string in a python dictionary
data = json.loads(post_codes_req)

# this will display the data that has been stored
# print(data)
# it has now converted the data into a python dictionary


# creating a class
class JSONReaderr:

    def get_all_values(self, nested_dictionary):  # This is a method
        for key, value in nested_dictionary.items():  # iterate through the key value pairs in this dictionary
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value)  # recall this method passing in that dictionary to iterate through it
        else:
            print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through

json_reader = JSONReaderr()  # Create instance of this function

json_reader.get_all_values(data)  # Returns all the values inside a dictionary including any nested dictionarie