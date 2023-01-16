"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
import ast

lukujono = []
x = 0

while (x == 0):
    uusiluku = input("Anna luku lukujonoon tai paina ENTER")
    if (uusiluku == ""):
        x = 1
    elif ((type(uusiluku) is int) or (type(uusiluku) is float)):
        lukujono.append(uusiluku)
    else:
        print("Uusi lukusi ei ollut luku. Koita uudestaan.")

print(lukujono)
#Tulosta pienin ja suurin.