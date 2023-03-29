"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
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
               f"Huippunopeus: {self.huippunopeus} km/h\n" \
               f"Tämänhetkien nopeus: {self.nopeus} km/h\n" \
               f"Kuljettu matka: {self.kulj_matka} km"

    def kiihdytä(self, nop_muutos):
        self.nopeus += nop_muutos

        # Nopeusrajoitin 0 - huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kulje(self, tunti):
        self.kulj_matka += self.nopeus * tunti


class Sähköauto(Auto):
    def __init__(self, rek: str, nop: int, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super().__init__(rek, nop)

    def __str__(self):
        return f"Auton tiedot:\n" \
               f"Rekisteritunnus: {self.rekisteritunnus}\n" \
               f"Huippunopeus: {self.huippunopeus} km/h\n" \
               f"Tämänhetkien nopeus: {self.nopeus} km/h\n" \
               f"Akun kapasiteetti: {self.kapasiteetti} kw/h\n" \
               f"Kuljettu matka: {self.kulj_matka} km\n"


class Polttomoottoriauto(Auto):
    def __init__(self, rek: str, nop: int, tilavuus):
        self.tilavuus = tilavuus
        super().__init__(rek, nop)

    def __str__(self):
        return f"Auton tiedot:\n" \
               f"Rekisteritunnus: {self.rekisteritunnus}\n" \
               f"Huippunopeus: {self.huippunopeus} km/h\n" \
               f"Tämänhetkien nopeus: {self.nopeus} km/h\n" \
               f"Bensatankin tilavuus: {self.tilavuus} l\n" \
               f"Kuljettu matka: {self.kulj_matka} km\n"


auto1 = Sähköauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

auto1.kiihdytä(125)
auto2.kiihdytä(150)
auto1.kulje(3)
auto2.kulje(3)

print(auto1)
print(auto2)
