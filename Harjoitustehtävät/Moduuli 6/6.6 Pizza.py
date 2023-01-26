"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
    ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
import math


def pizzalaskuri(halkaisija, hinta):
    pinta_ala = math.pi * halkaisija
    hinta_ala = hinta / pinta_ala
    return hinta_ala


halk = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hint = float(input("Anna ensimmäisen pizzan hinta (€): "))
ekapizza = pizzalaskuri(halk, hint)

halk = float(input("Anna toisen pizzan halkaisija (cm): "))
hint = float(input("Anna toisen pizzan hinta (€): "))
tokapizza = pizzalaskuri(halk, hint)

print(f"Eka pizza = {round(ekapizza, 3)} € / cm^2 \nToka pizza = {round(tokapizza, 3)} € / cm^2")
if ekapizza > tokapizza:
    print("Eka pizza on parempi vastine rahalle.")
elif tokapizza > ekapizza:
    print("Toka pizza on parempi vastine rahalle.")
else:
    print("Pizzat ovat yhtä hyviä vastineita rahalle.")