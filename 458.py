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

a = min(hulk.intelligence, captain_america.intelligence, thanos.intelligence)
print(a)
stat_dict = {"Hulk" : hulk.intelligence, "Captain America" : captain_america.intelligence, "Thanos" : thanos.intelligence}
for key, value in stat_dict.items():
    if value == a:
        print(f"Самый умный персонаж: {key}")

