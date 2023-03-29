"""
Toteuta seuraava luokkahierarkia Python-kielellä:
Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        # print all
        print(f"{'-'*40}\n"
              f"{'Kirjan nimi: ':<25} {self.nimi:>15}\n"
              f"{'Kirjan kirjoittaja: ':<25} {self.kirjoittaja:>15}\n"
              f"{'Kirjan sivumäärä: ':<25} {self.sivut:>15}\n"
              f"{'-'*40}")


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        # print all
        print(f"{'-'*40}\n"
              f"{'Lehden nimi: ':<25} {self.nimi:>15}\n"
              f"{'Lehden päätoimittaja: ':<25} {self.toimittaja:>15}\n"
              f"{'-'*40}")


akkari = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

akkari.tulosta_tiedot()
hytti.tulosta_tiedot()
