import requests
import json

# Token = 2619421814940190


def request():
    url = "https://superheroapi.com/api/2619421814940190/search/"
    params = {}
    return = requests.get(url, params=params, timeout=5)



