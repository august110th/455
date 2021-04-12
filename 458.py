import requests
import json

# def __init__(self, token):
#   self.token = token
#
# def get_headers(self):
#   return {
#
#
#   }
#
#
#
#
#
#
#
#


Token = 2619421814940190


def request():
    url = "https://superheroapi.com/api/2619421814940190/search/"
    params = {"name": "Hulk"}
    headers = {"Authorization": "Token"}
    return requests.get(url, params=params, headers=headers, timeout=5)

if __name__ == "__main__":
  print(request().json())


