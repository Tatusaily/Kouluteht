import random

#random maat
maat = {
    1: "pata",
    2: "hertta",
    3: "ruutu",
    4: "risti"
}
class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

kortti1 = Pelikortti(maat[random.randint(1, 4)], random.randint(1, 14))
kortti2 = Pelikortti

print(kortti1.maa)
print(kortti1.arvo)
