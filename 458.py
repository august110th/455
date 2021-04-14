import requests

class Hero():

    def __init__(self, name):
        self.intelligence = 0
        self.id = 0
        self.name = name

    def hero_stat(self):
        hero_dict = requests.get(("https://superheroapi.com/api/2619421814940190/search/") + self.name).json()
        self.intelligence = hero_dict['results'][0]['powerstats']["intelligence"]
        self.id = hero_dict['results'][0]['id']
        # stat_dict = {}
        # stat_dict[self.name] += [self.intelligence]
        print(hero_dict)
        # print(stat_dict)
hulk = Hero("Hulk")
captain_america = Hero("Captain America")
thanos = Hero("Thanos")

hulk.hero_stat()
# captain_america.hero_stat()
# thanos.hero_stat()

# print(stat_dict)
# def stat_dict_get(Hero):
#     stat_dict = {}
#





# def request():
#     url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
#     params = {}
#     return requests.get(url, params=params, timeout=5)
# print(request().json())



# #     return
# # hero_intelligence()
# print(hero_int)
# print(hero_id)
