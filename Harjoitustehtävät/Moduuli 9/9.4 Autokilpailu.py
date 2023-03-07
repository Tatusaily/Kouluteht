"""
Nyt ohjelmoidaan autokilpailu.
Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
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

    def kulje(self,tunti):
        self.kulj_matka += self.nopeus * tunti

        return


# Pääohjelma
# Tehdään kisaan osallistuvat autot
autodict = {}
for n in range(1,11):
    rek = f"ABC-{n:03d}"
    nop = random.randint(100,200)
    autodict[f"Auto{n}"] = Auto(rek, nop)

maalissa = False
kisa = True
while kisa == True:  # Tähän vois kirjottaa while kisa: mutta se on mun mielestä vähän huonosti luettavaa
    for auto in autodict.values():
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kulj_matka >= 10000:
            maalissa = True
    if maalissa == True:
        kisa = False
        print(f"Kisa on ohi!\n")


# Kisa on ohi, tulostetaan taulukko
# Tehdään tosi siisti otsikko:
print(f"{'LOPPUTILANNE':{'-'}{'^'}{72}}\n"
      f"||{'Rekisteri':^15}|{'Matka':^15}|{'Nopeus':^15}|{'Huippunopeus':^20}||\n"
      f"{'-'*72}")
# Ja sitten täytetään taulukkoon data
for auto in autodict.values():
    print(f"||{auto.rekisteritunnus:^15}|{str(auto.kulj_matka)+' km':^15}|"
          f"{str(auto.nopeus)+' km/h':^15}|{str(auto.huippunopeus)+' km/h':^20}||\n"
          f"{'-'*72}")
