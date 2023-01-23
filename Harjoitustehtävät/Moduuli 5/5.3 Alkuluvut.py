"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

luku = int(input("Anna luku. Testataan onko se alkuluku.  "))
on_alku = True
if luku == 1:
    print("1 Ei ole alkuluku.")
elif luku == 2:
    print("2 On alkuluku")
else:
    for i in range(2, luku - 1):
        if (luku % i == 0):
            print(f"{luku} On jaollinen luvulla {i}!")
            print(f"{luku} / {i} = {luku/i}")
            on_alku = False
            break
    if on_alku == True:
        print(f"{luku} On alkuluku!")
    else:
        print(f"{luku} Ei ole alkuluku!")


