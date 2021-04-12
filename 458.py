import requests
Token = 2619421814940190
def request():
  url = "https://superheroapi.com/api/2619421814940190/search/name"
  params = {"name" : "hulk"}
  headers = {"Authorization" : "Token"}
  response = request.get(url, params=params, headers=headers, timeout=5)
  print(response)