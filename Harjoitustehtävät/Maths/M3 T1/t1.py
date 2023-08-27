import math

# Funktiot joilla muutetaan radiaanit asteiksi tai toisin päin

def radtodeg(rad: float):
    deg = (rad * (180/math.pi))
    return deg


def degtorad(deg: float):
    rad = (deg * (math.pi/180))
    return rad


# Tulostukset
# T1
print(f"1. Muunna asteiksi:\n"
      f"a) 2,493 rad = {radtodeg(2.493):.1f} astetta.\n"
      f"b) 0,911 rad = {radtodeg(0.911):.1f} astetta\n")

# T2
print(f"2. Muunna radiaaneiksi:\n"
      f"a) 137,7° = {degtorad(137.7):.1f} rad.\n"
      f"b) 62,3° = {degtorad(62.3):.1f} rad\n")

# T3
print("3. Tee taulukko: ")
deglist = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for i in deglist:
    print(f"{i}° = {degtorad(i):.2f} rad")
print("")

# T4
print("Kolmio:")
kateetti1 = 2.3
kateetti2 = 4.7
hypotenuusa = math.sqrt(kateetti1**2 + kateetti2**2)  # Hypotenuusan neliö = sivujen neliöiden summa. Neliöjuuri = pituus
kulma1 = math.asin(kateetti1/hypotenuusa)
kulma2 = math.asin(kateetti2/hypotenuusa)

print(f"Sivut ovat {kateetti1} ja {kateetti2}.")
print(f"Hypotenuusa = {hypotenuusa:.1f}")
print(f"Kulmat ovat: {radtodeg(kulma1):.1f}° "
      f"ja {radtodeg(kulma2):.1f}°\n")

# T5
print("Kertomat:")
print(f"0! = {math.factorial(0)}")
print(f"4! = {math.factorial(4)}")
print(f"7! = {math.factorial(7)}")
print(f"15! = {math.factorial(15)}")
