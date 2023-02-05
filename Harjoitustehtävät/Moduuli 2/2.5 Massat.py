import math
#Kysy yksiköt
leiviska_in =    float(input("Montako leiviskää?"))
naula_in =       float(input("Montako naulaa?"))
luoti_in =       float(input("Montako luotia?"))

#Lasku ja tulostus
grammat =       luoti_in*13.3 + naula_in*13.3*32 + leiviska_in*13.3*32*20
kilot =         math.floor(grammat/1000)
print("Massa kiloissa ja grammoissa:")
print(kilot, "kiloa ja ", round(grammat-kilot*1000, 1), "grammaa.")
round(x, y)