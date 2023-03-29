"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""
import random

arpa = random.randint(1, 10)
oikein = 0
print("Arvoin kokonaisluvun väliltä 1 - 10.")
print("Arvaatko mitä lukua ajattelen?")

while oikein != 1:
    arvaus = int(input("Anna arvauksesi: "))
    if arvaus == arpa:
        break
    elif arvaus > arpa:
        print("Arvauksesi oli liian korkea. Koeta uudestaan!")
    else:
        print("Arvauksesi oli liian vähän. Koeta uudestaan!")

print(f"Oikein! Ajattelin lukua {arpa}!")