"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä
jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random


def noppakuusi(tahkot):
    return random.randint(1, tahkot)


noppa = 0
lukum = 0
tahkot_input = int(input("Moniko sivuista noppaa heitetään? "))
while noppa != tahkot_input:
    print("Heitetään noppaa:")
    noppa = noppakuusi(tahkot_input)
    lukum += 1
    print(f"Nopan silmäluvuksi tuli: {noppa}\n")
print(f"Noppaa täytyi heittää {lukum} kertaa.")
