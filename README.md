## JSON
- Javascript Object Notation

- Syntax - json in itself is syntax for exchanging data 

_Where and how?_

- between browser and server

_What type of data?_

- The data can only be text- json is text written in json format 
`a string`
`a number` 
`an object (json object)`
` an array`
`a boolean, value`

_Where does this syntax derive from javascript?_
- Data is stored in key value pairs - here its called name/value pairs:

```python
{"name": "james", "age":"21"}
```
- data is separated by , 

- ** json is also used to pass data from existing files or web browser

```python
import json


# ENCODING from dictionary and writing to jsonfile
car_data = {"name":"tesla", "engine":"electric"}
print(car_data)
# printing the dictionary

# checking the type of a dictionary
print(type(car_data))

car_data_json_string = json.dumps(car_data)
# json.dumps changes python dict to json str

# so now when we print it will show it as a string
print(type(car_data_json_string))

# Let's create a jsonfile with writing permission
with open("new_json_file.json", "w") as jsonfile: # using aliasing
    # enter the name of the file

    json.dump(car_data, jsonfile) # json dump
    # dump takes 2 arguments:
          # first is the dictionary
          # second is the file object = jsonfile on this occasion

# this will produce no new outcome when running the file
# however this will create new file in folder called "new_json_file"
# ENCODING(creating & writing) into json file

with open("new_json_file.json") as jsonfile: # DECODING
# Reading from the file we just created
    car = json.load(jsonfile) # storing data from file to car variable
    print(type(car)) # checking the type of data again
    print(car['name']) # get the value stored name
    print(car['engine']) # get the value stored in second value pair

# we have DECODED(reading) file new_json.json that we created earlier
# we have used following methods: dumps(), dump(), and load ()
```
 
* dealing with secret data- data that is encoded in data that is in format that's' not readable