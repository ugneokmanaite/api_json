import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(post_codes_req.status_code) # just status code
# print(post_codes_req.content) # contents
# print(type(post_codes_req)) # body
# print(post_codes_req.headers) #headers
# print(type(post_codes_req.headers))
# print(post_codes_req.json())
json_data = post_codes_req.json()
# storing data from json()

for key in json_data:
    print(key)
print(type(json_data))
print(json_data)

# exercise is to fetch data by key value pairs within dictionaries
# create a function to return the above values (key:value)
# create a class and move the code block inside the class

def fetch_data:



# why should we use built in packages
# they come with amazing functionalities already available

# first iteration
# if post_codes_req.status_code == 200:
#     print(" success ")
# elif post_codes_req.status_code == 400:
#     print (" sorry page not available")

# second iteration
# shows why we should use built in packages!
# if post_codes_req.status_code:
#     print(" success ")
# elif post_codes_req.status_code:
#     print (" sorry page not available")

# third iteration - create same functionality with OOP
# class and a method

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")


# class Live_Web_status:
#
#     def __init__(self):
#         pass
#
#     def check_status_code():
#         if post_codes_req.status_code:
#             return "success "
#         elif post_codes_req.status_code:
#             return "sorry page not available"
#
#
# status = Live_Web_status()  # creating a class object/instantiating
# print(status.check_status_code())  # calling the method
