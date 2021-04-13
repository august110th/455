import requests

class Hero():

    def __init__(self, intelligence, id, name):
        self.intelligence = intelligence
        self.id = id
        self.name = name

    def hero_stat(self):
        hero_dict = requests.get(("https://superheroapi.com/api/2619421814940190/search/Hulk") + self.name).json()
        self.intelligence = hero_dict['results'][0]['powerstats']["intelligence"]
        self.id = hero_dict['results'][0]['id']
        print(hero_dict)



# def request():
#     url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
#     params = {}
#     return requests.get(url, params=params, timeout=5)
# print(request().json())



# #     return
# # hero_intelligence()
# print(hero_int)
# print(hero_id)
