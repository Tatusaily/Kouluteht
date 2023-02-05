"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
 sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen."""

import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def GetAirport(ICAO):
    ICAO = ICAO.upper()
    query = f"SELECT name, municipality from airport WHERE ident= '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    return tulos

koodi = input("Anna ICAO koodi: ")
kenttä = GetAirport(koodi)
tuloskent = kenttä[0]
print(f"{tuloskent[0]}, {tuloskent[1]}.")


