"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
    hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
"""
inp = 0
kentat = {}

#Haluatko (S)yöttää (H)akea vai (L)opettaa?
while inp != "" or inp != "L":
    inp = input("Haluatko (S)yöttää (H)akea vai (L)opettaa? ")
    inp = inp.upper()
    if inp[0] == "S":
        #SYÖTTÖ
        ICAOs = input("Anna kentän ICAO -tunnus. ")
        NIMIs = input("Anna kentän nimi. ")
        kentat[ICAOs] = NIMIs

    elif inp[0] == "H":
        #HAKU
        ICAOh = input("Anna haettavan kentän ICAO -tunnus: ")
        if ICAOh == "*":
            for key in kentat:
                print(f"{key} - - {kentat[key]}")
        else:
            print(f"{ICAOh} - - {kentat[ICAOh]}")

    elif inp[0] == "L":
        #LOPETUS
        quit(print("Lopetetaan:"))
