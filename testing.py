from json_parsing_with_api import Live_Web_status

import requests

class Testing(Live_Web_status):
    def __init__(self):

        super().__init__()


bbc_req = requests.get("https://www.bbc.com/")

# import requests
# # Iteration 2, doing same output with oop
# class Status_code:
#     # Getting user input of url
#     def __init__(self, url):
#         self.url = url
#     def check_status_code(self):
#         # Getting status of website, using requests function
#         self.post_codes_req = requests.get(self.url)
#         print(self.post_codes_req.status_code)
# class Live_web_status(Status_code):
#     # Inheriting url attribute from Status_code class
#     def __init__(self, url):
#         super().__init__(url)
#     def live_web_status(self):
#         # Calling function from parent class to get status code of the website
#         self.check_status_code()
#         # Dont need to manually declare == 200, built in packages do it already
#         if self.post_codes_req.status_code == 200:
#             print("It worked!")
#         elif self.post_codes_req.status_code:
#             print("Page not available")
# obj1 = Live_web_status("https://api.postcodes.io/postcodes/se120nb")
# obj1.live_web_status())

