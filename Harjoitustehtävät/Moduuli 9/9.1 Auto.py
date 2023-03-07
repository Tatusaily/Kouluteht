"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi
ensin mainittua parametreina saatuihin arvoihin
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""


class Auto:
    def __init__(self, rek: str, nop: int):
        self.rekisteritunnus = rek
        self.huippunopeus = nop
        self.nopeus = 0
        self.kulj_matka = 0

    def __str__(self):
        return f"Auton tiedot:\n" \
               f"Rekisteritunnus: {self.rekisteritunnus}\n" \
               f"Huippunopeus: {self.huippunopeus}\n" \
               f"Tämänhetkien nopeus: {self.nopeus}\n" \
               f"Kuljettu matka: {self.kulj_matka}"


# Pääohjelma
uusiauto = Auto("ABC-123", 142)
print(uusiauto)
