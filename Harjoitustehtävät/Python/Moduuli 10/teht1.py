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


if __name__ == '__main__':
    hissi1 = Hissi(15, 1)
    hissi1.siirry_kerrokseen(200)
    hissi1.siirry_kerrokseen(3)
    hissi1.siirry_kerrokseen(5)
    hissi1.siirry_kerrokseen(5)
    hissi1.siirry_kerrokseen(1)
