"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
    kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
"""

luvut = []

uusiluku = (input("Anna uusi luku tai paina ENTER jatkaaksesi:  "))
while uusiluku != "":
    try:
        uusiluku = float(uusiluku)
        if uusiluku % 1 == 0.0:
            uusiluku = int(uusiluku)
        luvut.append(uusiluku)
    except:
        print("Syötäthän vain kokonaislukuja tai desimaaleja.")
    uusiluku = (input("Anna uusi luku tai paina ENTER jatkaaksesi.  "))

luvut.sort(reverse=True)
print(f"{luvut[:5]}")