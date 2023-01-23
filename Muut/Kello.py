import math
def kello(x):
    tunnit = math.floor(x / 3600)
    x -= tunnit*3600
    minuutit = math.floor(x / 60)
    x -= minuutit*60
    print(f"{tunnit:02d}:{minuutit:02d}:{x:02d}")

sekunnit = int(input("Montako sekuntia laitetaan? "))
kello(sekunnit)