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

hulk = Hero("Hulk")
captain_america = Hero("Captain America")
thanos = Hero("Thanos")

hulk.hero_stat()
captain_america.hero_stat()
thanos.hero_stat()

stat_dict = {"Hulk" : hulk.intelligence, "Captain America" : captain_america.intelligence, "Thanos" : thanos.intelligence}
sorted_dict = {}
sorted_keys = sorted(stat_dict, key=stat_dict.get)
for w in sorted_keys:
    sorted_dict[w] = stat_dict[w]
print(sorted_dict)
keys = list(sorted_dict.keys())
print(f"Самый умный персонаж: {keys[0]}")
