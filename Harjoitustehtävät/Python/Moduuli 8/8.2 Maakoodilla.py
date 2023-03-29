"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
"""

import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )
def GetAirport(ISO):
    ISO = ISO.upper()
    query = f"SELECT type, count(type) FROM airport WHERE iso_country= '{ISO}' GROUP BY type;"
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    return tulos

ISO = input("Anna maakoodi: ")
print("")
tulokset = GetAirport(ISO)
print(f"{'Tyyppi':<18} {'Lukumäärä':>14}")
for t in tulokset:
    print(f"{t[0]:<20} {t[1]:>12}")

