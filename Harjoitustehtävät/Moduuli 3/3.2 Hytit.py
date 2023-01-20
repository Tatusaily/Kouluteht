#Kysyy hyttiluokan
hyttivalinta = str.upper(input("Mikä on hyttiluokkasi?"))

#Hyttien kuvaukset
hyttilux = "LUX on parvekkeellinen hytti yläkannella."
hyttia = "A on ikkunallinen hytti autokannen yläpuolella."
hyttib = "B on ikkunaton hytti autokannen yläpuolella."
hyttic = "C on ikkunaton hytti autokannen alapuolella."

#Hyttikuvauksen anto
if hyttivalinta == "LUX":
    print(hyttilux)
elif hyttivalinta == "A":
    print(hyttia)
elif hyttivalinta == "B":
    print(hyttib)
elif hyttivalinta == "C":
    print(hyttic)
else:
    print("Virheellinen Hyttiluokka!")