"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka
jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""


vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

#Kysytään käyttäjältä kuukauden numero:
kuukausi = int(input("Anna kuukauden numero: "))

#Katsotaan mihin vuodenaikaan kuukausi kuuluu.
    #12, 1, 2 = Talvi
    #3, 4, 5 = Kevät
    #6, 7, 8 = Kesä
    #9, 10, 11 = Syksy

#Tulostetaan vastaava vuodenaika.
#Print(vuodenaika)