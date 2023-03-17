import math


def radtodeg(rad: float):
    deg = (rad * (180/math.pi))
    return deg


def degtorad(deg: float):
    rad = (deg * (math.pi/180))
    return rad


vastaus = input("A = asteet radiaaneiksi:\n"
                "R = radiaanit asteiksi: ")

if vastaus == "A":
    print(degtorad(float(input())))
elif vastaus == "R":
    print(radtodeg(float(input())))
