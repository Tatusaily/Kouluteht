"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen palauttaman summan.
"""
import random
def summalist(x):
    return(sum(x))
def randomi(lukum, raja):
    for i in range(lukum):
        lista.append(random.randint(1, raja))

lista = []
lukum = int(input("Montako lukua haluat lisätä listaan? "))
raja = int(input("Minkä haluat suurimmaksi mahdolliseksi luvuksi? "))
print(f"Luon nyt listaan {lukum} lukua väliltä 1 - {raja} \n")
randomi(lukum, raja)
print(lista)
print(f"Listan summa on: {summalist(lista)}")