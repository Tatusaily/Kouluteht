import math
"""
Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""
n = 1
yläraja = 1000
x = 0
jaolliset = []
while n <= yläraja:
    if n % 3 == 0:
        jaolliset.append(n)
    n += 1
for i in jaolliset:
    print(i,"", end = '') #end poistaa printin perästä sen automaattisen linebreakin.
    x += 1
    if x == 3:            #printataan joka kolmas luku linebreak.
        print("")
        x = 0
