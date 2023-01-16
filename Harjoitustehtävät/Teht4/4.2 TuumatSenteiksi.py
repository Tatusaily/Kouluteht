"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin
kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""

#Ota tuumat
tuumat = input("Anna tuumat. ")
sentit = 0.0
try:
    tuumat = float(tuumat)
except:
    print("Anna tuumat numeroina!")
    quit()
#Onko negatiivinen?
if tuumat < 0:
    print("Ohjelma sammuu, koska tuumat ovat negatiivisia.")
    quit()
else:
#Muuta senteiksi ja print
    sentit = tuumat*2.54
    print(f"{sentit:.2f}")