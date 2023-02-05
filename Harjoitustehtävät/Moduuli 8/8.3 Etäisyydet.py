"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def GetAirportCoords(ICAO):
    ICAO = ICAO.upper()
    query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '{ICAO}';"
    cursor = yhteys.cursor()
    cursor.execute(query)
    result = cursor.fetchone()  #fetchone palauttaa ensimmäisen(seuraavan) rivin taulusta tuplena.
    return result

coordinates = []
for n in range(2):
    icaoinput = input("Anna ICAO koodi: ")






