"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja
muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

Yksi gallona on 3,785 litraa.
"""

def gallon_litra(gallonat):
    litrat = gallonat*3.785
    return litrat


go = True
valinta = int(input("Anna gallonat niin muutan ne litroiksi: "))

while go:
    if gallon_litra(valinta) < 0:
        go = False
        quit(print("Annoit negatiivisen luvun. Suljetaan."))
    else:
        print(round(gallon_litra(valinta), 2))
        valinta = int(input("Anna gallonat, niin muutan ne litroiksi. "))