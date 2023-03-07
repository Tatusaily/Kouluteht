"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi,
joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin
auto on tasaisella vauhdilla annetussa  tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
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

    def kulje(self,tunti):
        self.kulj_matka += self.nopeus * tunti

        return

# Pääohjelma
uusiauto = Auto("ABC-123", 142)
print(f"{uusiauto}\n")

uusiauto.kiihdytä(30)
uusiauto.kulje(2)
print(f"{uusiauto}\n")