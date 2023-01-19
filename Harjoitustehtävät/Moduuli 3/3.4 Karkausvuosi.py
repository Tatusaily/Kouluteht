"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
"""
try:
    vuosi = int(input("Anna vuosiluku."))
except:
    quit(print("Anna vuosiluku numeroina kokonaislukuna."))

if vuosi % 4 != 0:
    print(f"Vuosi ei ole karkausvuosi")
elif vuosi % 100 == 0 and vuosi % 400 != 0:
    print(f"Vuosi ei ole karkausvuosi")
else:
    print(f"Vuosi on karkausvuosi!")