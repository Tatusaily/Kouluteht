"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

sukupuoli = str.lower(input("Oletko biologiselta sukupuoleltasi mies vai nainen?"))
hemoglobi = float(input("Mikä on hemoglobiiniarvosi? (g/l)"))

if (sukupuoli == "mies" and hemoglobi > 195) or (sukupuoli == "nainen" and hemoglobi > 175):
    print(f"Hemoglobiiniarvosi on korkea!")
elif (sukupuoli == "mies" and hemoglobi < 134) or (sukupuoli == "nainen" and hemoglobi < 117):
    print(f"Hemoglobiiniarvosi on alhainen!")
elif sukupuoli == "mies" or sukupuoli == "nainen":
    print(f"Hemoglobiiniarvosi on normaali!")
else:
    print("Tapahtui virhe")
