#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
import math
print("Anna ympyrän halkaisija, niin lasken sen pinta-alan.\n")

#Otetaan ympyrän halkaisija ja muutetaan käyttäjän antama arvo floatiksi.
radius_str = input()
radius = float(radius_str)

#Lasketaan ympyrän pinta-ala ja kerrotaan se takaisin käyttäjälle.
area = math.pi * pow(radius, 2)
print("Ympyräsi pinta-ala on %f"%area)
