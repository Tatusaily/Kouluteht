"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""
import random

#Tehdään rand.luku ja yhteenlasketaan se aina vanhan päälle.
nopat = int(input("Montako noppaa heitetään? "))
kokonais = 0
for x in range(nopat):
    uusiluku = random.randint(1, 6)
    kokonais += uusiluku

print(f"Noppien silmälukujen summa on: {kokonais}")
