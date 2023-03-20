"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""


class Hissi:
    def __init__(self, ylin, alin):
        self.ylinkerros = ylin
        self.alinkerros = alin
        self.nykyinenkerros = alin

    def kerros_ylös(self):
        self.nykyinenkerros += 1
        return

    def kerros_alas(self):
        self.nykyinenkerros -= 1
        return

    def siirry_kerrokseen(self, kerros):
        # Tarkistetaan syöte
        if kerros < self.alinkerros or kerros > self.ylinkerros:
            print(f"{kerros}. kerros ei ole saatavilla\n")
            return
        # Siirrytään
        if kerros != self.nykyinenkerros:
            print(f"Nykyinen kerros:{self.nykyinenkerros}")
            if kerros > self.nykyinenkerros:
                while kerros > self.nykyinenkerros:
                    print(f"Noustaan ylöspäin...")
                    self.kerros_ylös()
            if kerros < self.nykyinenkerros:
                while kerros < self.nykyinenkerros:
                    print(f"Laskeudutaan alaspäin...")
                    self.kerros_alas()
            print(f"Ollaan nyt kerroksessa {self.nykyinenkerros}\n")
        else:
            print(f"Hissi on jo valitussa kerroksessa.\n")
        return


class Talo:
    def __init__(self, ylinkrs: int, alinkrs: int, hissit: int):
        # Tehdään talolle hissit
        self.ylinkrs = ylinkrs
        self.alinkrs = alinkrs
        self.hissilista = []
        for n in range(hissit):
            uusihissi = Hissi(ylinkrs, alinkrs)
            self.hissilista.append(uusihissi)

    def aja_hissiä(self, hissinro: int, kohdekerros: int):
        print(f"Siirretään hissi {hissinro} kerrokseen {kohdekerros}")
        self.hissilista[hissinro-1].siirry_kerrokseen(kohdekerros)


if __name__ == '__main__':
    isotalo = Talo(20, 1, 5)
    print(f"Luotiin talo jossa on {isotalo.ylinkrs} kerrosta ja {len(isotalo.hissilista)} hissiä.")

    print(f"Ajetaan talon 2. hissiä kerrokseen 10:")
    isotalo.aja_hissiä(2, 10)




