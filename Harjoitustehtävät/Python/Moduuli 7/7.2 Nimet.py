"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko
tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
"""

nimi = "0"
nimet = set()

while nimi != "":
    nimi = input("Anna nimi: ")
    if nimi in nimet:
        print(f"Aiemmin syötetty nimi.")
    elif nimi != "":
        nimet.add(nimi.capitalize())
        print(f"Uusi nimi.")

print("")
print("Tulostetaan nimet: ")
for n in nimet:
    print(n)