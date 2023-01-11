import random
print("Arvon nyt kaksi numerolukon koodia:")

ekakoodi = []
for i in range(3):
    ekakoodi.append(random.randint(0, 9))
print(ekakoodi)

tokakoodi = []
for i in range(4):
    tokakoodi.append(random.randint(1, 6))
print(tokakoodi)