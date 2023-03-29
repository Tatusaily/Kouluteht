"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
    (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
Käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
"""

kaupungit = []

for i in range(5):
    city = input("Anna kaupungin nimi. ")
    print(f"Syötetään {city} listaan.\n")
    kaupungit.append(city)

for i in kaupungit:
    print(i)