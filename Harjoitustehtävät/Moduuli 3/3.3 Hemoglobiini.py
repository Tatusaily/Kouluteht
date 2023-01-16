"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

sukupuoli = str.lower(input("Oletko biologiselta sukupuoleltasi mies vai nainen?"))
hemoglobi = float(input("Mikä on hemoglobiiniarvosi? (g/l)"))
if sukupuoli == "mies" or sukupuoli == "nainen":
    if sukupuoli == "mies":
        if hemoglobi > 195:
            print(f"Hemoglobiiniarvosi on korkea!")
        elif hemoglobi < 134:
            print(f"Hemoglobiiniarvosi on alhainen!")
        else:
            print(f"Hemoglobiiniarvosi on normaali!")
    if sukupuoli == "nainen":
        if hemoglobi > 175:
            print(f"Hemoglobiiniarvosi on korkea!")
        elif hemoglobi < 117:
            print(f"Hemoglobiiniarvosi on alhainen!")
        else:
            print(f"Hemoglobiiniarvosi on normaali!")
else: print('Tämä ohjelma toimii vain jos ilmoitat biologiseksi sukupuoleksesi "mies" tai "nainen".')
