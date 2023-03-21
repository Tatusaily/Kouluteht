import requests

vastaus = requests.get("https://api.chucknorris.io/jokes/random").json()
print(vastaus["value"])
