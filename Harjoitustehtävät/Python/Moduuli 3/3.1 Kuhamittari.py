"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
    ilmoittaen samalla käyttäjälle, montako senttiä alimmasta
    sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

KuhanPituus = input("Kuinka pitkä kuhasi on senttimetreissä? ")
pituusraja = 37

#Testaa onko käyttäjän syöttämä pituus numero. (voiko siitä tehdä floatin)
try:
    KuhanPituus = float(KuhanPituus)
except:
    quit(print("Anna kuhan pituus numeroina."))

if KuhanPituus >= pituusraja:
    print("Hieno kala!")
else:
    print("Kuhasi on", pituusraja-KuhanPituus, "senttiä liian lyhyt. Päästetään se takaisin järveen.")