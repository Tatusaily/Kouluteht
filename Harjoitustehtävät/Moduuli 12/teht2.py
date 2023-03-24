"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
    ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
"""
import requests
import json


def kelvin_to_celcius(kelvin):
    celcius = (-273.15)+kelvin
    celcius = celcius.__round__(1)
    return celcius


def get_coords(cityname):
    query = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit={5}&appid={API_KEY}")
    # Täältä tulee lista dictejä
    print("Saatu yhteys.\n")
    return query.json()


def get_weather(city):
    lat = city['lat']
    lon = city['lon']
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=fi").json()
    climate = weather['weather'][0]['description']
    temp = weather['main']['temp']
    temp = kelvin_to_celcius(temp)
    name = weather['name']
    return name, climate, temp


# API KEY
API_KEY = "337b16224b8ccdfd01fba013b925b025"

# Haetaan tieto, tulostetaan kaupungit ja otetaan käyttäjän valinta
cityn = input("Nimi")
vastaus = get_coords(cityn)
n = 0
for result in vastaus:
    print(f"{n+1}. Kaupunki: {result['name']} "
          f"Koordinaatit: ({result['lat']} lat, {result['lon']} lng) "
          f"Maa: {result['country']}")
    n += 1
print("")
sää = get_weather(vastaus[int(input("Valitse Kaupunki: "))-1])

# Tulostetaan säätiedot
print(f"Kaupungin nimi: {sää[0]}")
print(f"Kuvaus säästä: {sää[1]}")
print(f"Lämpötila {sää[2]} °C")
