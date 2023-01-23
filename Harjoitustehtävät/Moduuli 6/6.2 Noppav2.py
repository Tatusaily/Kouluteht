"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä
jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random
noppa = 0
def noppakuusi(tahkot):
    return random.randint(1, tahkot)

tahkot_input = int(input("Moniko sivuista noppaa heitetään? "))
while noppa != tahkot_input:
    print("Heitetään noppaa:")
    noppa = noppakuusi(tahkot_input)
    print(f"Nopan silmäluvuksi tuli: {noppa}\n")
