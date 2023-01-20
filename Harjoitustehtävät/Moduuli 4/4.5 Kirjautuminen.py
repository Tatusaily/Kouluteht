"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai
    väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""

tunnus_oikea = "python"
salasana_oikea = "rules"
tunnus1 = ""
salasana1 = ""
i = 1

while i <= 5:
    tunnus1 = input("Anna käyttäjätunnus: ")
    salasana1 = input("Anna salasana: ")
    if tunnus1 == tunnus_oikea and salasana1 == salasana_oikea:
        break
    i += 1

if tunnus1 == tunnus_oikea and salasana1 == salasana_oikea:
    print("Tervetuloa!")
else:
    print("Pääsy evätty.")