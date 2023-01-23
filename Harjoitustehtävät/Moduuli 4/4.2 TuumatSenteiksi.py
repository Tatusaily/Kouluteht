"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin
kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""

#Ota tuumat
tuumat = ""
sentit = 0.0
x = True

while x == True:
    tuumat = input("Anna Tuumat: ")
    try:
        tuumat = float(tuumat)
    except:
        print("Anna tuumat numeroina!")
        quit()
    if tuumat < 0:
        print("Ohjelma sammuu, koska tuumat ovat negatiivisia.")
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} Tuumaa = {sentit} senttiä.\n")
sentit = tuumat * 2.54
print(f"{tuumat} Tuumaa = {sentit} senttiä.")