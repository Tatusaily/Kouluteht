import numpy as np

# Tehdään matriisit
Array_A = np.array([[-1, 2], [3, -5]])
Array_B = np.array([[2, 0], [-1, 4]])

# Tulostetaan matriisit laskutoimituksineen
print(f"2A+3B =\n"
      f"{2*Array_A+3*Array_B}\n")
print(f"A-B =\n"
      f"{Array_A-Array_B}")
