"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random
noppa = 0
def noppakuusi():
    return random.randint(1, 6)

while noppa != 6:
    print("Heitetään noppaa:")
    noppa = noppakuusi()
    print(f"Nopan silmäluvuksi tuli: {noppa}\n")
