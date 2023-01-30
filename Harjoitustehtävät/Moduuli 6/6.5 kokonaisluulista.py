"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
 Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
 parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
jälkeen sekä alkuperäisen että karsitun listan.
"""
import random


def karsija(raakalista):
    uusilista = []
    for i in raakalista:
        if i % 2 == 0:
            uusilista.append(i)
    return uusilista


primary_list = []
lukum = int(input("Montako lukua luodaan listaan? "))

#Arvotaan {lukum} satunnaista lukua väliltä 1 - 99
#Laitetaan ne listaan
for n in range(lukum):
    primary_list.append(random.randint(1, 99))

karsittu_lista = karsija(primary_list)

#Kutsutaan karsijaa ja karsitaan primary_list
print(f"Tehtiin lista {primary_list}. Laitettiin se karsijan läpi: \n")
print(karsittu_lista)
