"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
lukujono = []
uusiluku = input("Anna luku lukujonoon tai paina ENTER")

# Tää kaatuu jos käyttäjä syöttää tekstiä.
while (uusiluku != ""):
    uusiluku = float(uusiluku)
    if uusiluku % 1 == 0.0:
        uusiluku = int(uusiluku)
    lukujono.append(uusiluku)
    uusiluku = input("Anna luku lukujonoon tai paina ENTER")

print(f"Pienin luku on {min(lukujono)} ja suurin on {max(lukujono)}.")