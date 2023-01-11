import math
#Kysy yksiköt
leiviskäIn=     float(input("Montako leiviskää?"))
naulaIn=        float(input("Montako naulaa?"))
luotiIn=        float(input("Montako luotia?"))

#Lasku ja tulostus
grammat=        luotiIn*13.3 + naulaIn*13.3*32 + leiviskäIn*13.3*32*20
kilot=          math.floor(grammat/1000)
print("Massa kiloissa ja grammoissa:")
print(kilot, "kiloa ja ", round(grammat-kilot*1000, 1), "grammaa.")