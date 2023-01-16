"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""

lukujono = []
x = 0

while (x == 0):
    uusiluku = input("Anna luku lukujonoon tai paina ENTER")
    if (uusiluku == ""):
        x = 1
    else:
        try:
            uusiluku = int(uusiluku)
            lukujono.append(uusiluku)
        except:
            print("Uusi luku ei ollut numero!")

print(lukujono)
#Tulosta pienin ja suurin.