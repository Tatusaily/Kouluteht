class Hissi:
    def __init__(self, ylin, alin):
        self.ylinkerros = ylin
        self.alinkerros = alin
        self.nykyinenkerros = alin
        print(f"Luotiin hissi, jonka ylimmät ja alimmat kerrokset ovat: {ylin} ja {alin}")

    def kerros_ylös(self):
        self.nykyinenkerros += 1
        return

    def kerros_alas(self):
        self.nykyinenkerros -= 1
        return

    def siirry_kerrokseen(self, kerros):
        # Tarkistetaan syöte
        if kerros < self.alinkerros or kerros > self.ylinkerros:
            print(f"Valittu kerros ei ole saatavilla")
            return
        print(f"Nykyinen kerros:{self.nykyinenkerros}")
        # Siirrytään
        if kerros != self.nykyinenkerros:
            if kerros > self.nykyinenkerros:
                while kerros > self.nykyinenkerros:
                    print(f"Noustaan ylöspäin...")
                    self.kerros_ylös()
            if kerros < self.nykyinenkerros:
                while kerros < self.nykyinenkerros:
                    print(f"Laskeudutaan alaspäin...")
                    self.kerros_alas()
            print(f"Ollaan nyt kerroksessa {self.nykyinenkerros}")
        else:
            print(f"Hissi on jo valitussa kerroksessa.")
        return


hissi1 = Hissi(10, 1)
hissi1.siirry_kerrokseen(200)
hissi1.siirry_kerrokseen(6)
hissi1.siirry_kerrokseen(1)

