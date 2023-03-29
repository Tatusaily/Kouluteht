from teht1 import Hissi


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

    def palohälytys(self):
        for hissi in self.hissilista:
            hissi.siirry_kerrokseen(self.alinkrs)


if __name__ == '__main__':
    isotalo = Talo(20, 1, 5)
    print(f"Luotiin talo jossa on {isotalo.ylinkrs} kerrosta ja {len(isotalo.hissilista)} hissiä.")

    print(f"Ajetaan isontalon 2. hissiä kerrokseen 10:")
    isotalo.aja_hissiä(2, 10)

    print("!PALOHÄLYTYS!")
    isotalo.palohälytys()
