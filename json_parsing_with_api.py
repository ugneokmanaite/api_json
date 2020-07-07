import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.status_code)
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

class

def check_status_code():
    if post_codes_req.status_code:
        print(" success ")
    elif post_codes_req.status_code:
        print (" sorry page not available")

