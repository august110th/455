import requests
import json

# Token = 2619421814940190


def request():
    url = "https://superheroapi.com/api/2619421814940190/search/"
    params = {}
    headers = {'Authorization': '2619421814940190'}
    return requests.get(url, params=params, headers=headers, timeout=5)



