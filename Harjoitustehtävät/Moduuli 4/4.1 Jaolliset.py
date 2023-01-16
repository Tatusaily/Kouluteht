import math
"""
Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""
n = 1
yläraja = 1000
jaolliset = []

# 12-15 Ottaa n arvon ja katsoo onko se jaollinen kolmella. Jos on niin laittaa sen listaan.
while n <= yläraja:
    if n % 3 == 0:
        jaolliset.append(n)
    n += 1

# 18-23 Tulostaa jaolliset listan niin, että halutun (y) rivimäärän jälkeen tehdään rivinvaihdos.
x = 1
y = 5
for i in jaolliset:
    print(i, "", end='')
    x += 1
    if x == y:
        print("")
        x = 0
