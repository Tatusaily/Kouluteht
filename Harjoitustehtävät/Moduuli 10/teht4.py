import random


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

        return


class Kilpailu:
    def __init__(self, nimi, pituus, autolkm):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujalista = []
        for n in range(autolkm):
            rekisteri = f"ABC-{n + 1}"
            huippunop = random.randint(100, 200)
            auto = Auto(rekisteri, huippunop)
            self.osallistujalista.append(auto)
        self.kulunutaika = 0

    def tunti_kuluu(self):
        for osallistuja in self.osallistujalista:
            osallistuja.kiihdytä(random.randint(-10, 15))
            osallistuja.kulje(1)
        self.kulunutaika += 1

    def tulosta_tilanne(self, teksti = "LOPULLINEN TILANNE"):
        print(f"{self.nimi.upper():{' '}{'^'}{72}}")
        print(f"{teksti:{'-'}{'^'}{72}}\n"
              f"||{'Rekisteri':^15}|{'Matka':^15}|{'Nopeus':^15}|{'Huippunopeus':^20}||\n"
              f"{'-' * 72}")
        for osallistuja in self.osallistujalista:
            print(f"||{osallistuja.rekisteritunnus:^15}|{str(osallistuja.kulj_matka) + ' km':^15}|"
                  f"{str(osallistuja.nopeus) + ' km/h':^15}|{str(osallistuja.huippunopeus) + ' km/h':^20}||\n"
                  f"{'-' * 72}")

    def kilpailu_ohi(self):
        ohi = False
        for osallistuja in self.osallistujalista:
            if osallistuja.kulj_matka >= 10000:
                ohi = True
        return ohi


kisa = Kilpailu("Suuri romuralli", 8000, 10)
while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    if kisa.kulunutaika % 10 == 0:
        kisa.tulosta_tilanne("VÄLITILANNE")
        print("")

kisa.tulosta_tilanne()

