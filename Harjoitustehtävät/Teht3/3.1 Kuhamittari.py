KuhanPituus = int(input("Kuinka pitkä kuhasi on senttimetreissä?"))
pituusraja = 37

if KuhanPituus >= pituusraja:
    print("Hieno kala!")
else:
    print("Kuhasi on", pituusraja-KuhanPituus, "senttiä liian lyhyt. Päästetään se takaisin järveen.")