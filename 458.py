import requests
import json

# Token = 2619421814940190


def request():
    url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
    params = {}
    return requests.get(url, params=params, timeout=5)
print(request().json())

# def hero_intelligence():
hero_dict = requests.get("https://superheroapi.com/api/2619421814940190/search/Hulk").json()
hero_int = hero_dict['results'][0]['powerstats']["intelligence"]
print(hero_dict)

#     return
# hero_intelligence()
print(hero_int)
