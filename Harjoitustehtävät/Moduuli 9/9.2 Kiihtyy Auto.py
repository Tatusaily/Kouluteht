"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
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

# Pääohjelma
uusiauto = Auto("ABC-123", 142)
print(f"{uusiauto}\n")

uusiauto.kiihdytä(30)
uusiauto.kiihdytä(70)
uusiauto.kiihdytä(50)
print(f"Auton tämänhetkinen nopeus: {uusiauto.nopeus} km/h")

uusiauto.kiihdytä(-200)
print(f"Auton lopullinen nopeus: {uusiauto.nopeus} km/h")