import numpy as np
import random

# T1
lista = np.array([])
for i in range(5):
    num = random.randint(1, 9)
    np.append(lista, num)

print(lista)
