from sympy import solve
from sympy.abc import x, y, z

# sympy haluaa yhtälöitä, joiden arvo = 0
# [-2x +y -z = -3]  -> [-2x +y -z +3]
set1a = solve([x - 2*y - 2*z,
               - 2*x + y - z + 3,
               3*x + 2*y + z - 4],
              x, y, z, dict=True)
set1b = solve([x + y - 1,
               2*x + y - z - 1,
               3*x + y - 2*z - 1],
              x, y, z, dict=True)
set2a = solve([2*x + 4*y - z - 11,
               6*x - y - 3*z - 7,
               3*x + 5*y - 2*x - 16],
              x, y, z, dict=True)
set2b = solve([4*x + 2*y - 2*z,
               2*x + y - z - 1,
               3*x + y - 2*z - 1],
              x, y, z, dict=True)

print(f"Osa 2 yhtälöryhmät:\n"
      f"1a = {set1a}\n"
      f"1b = {set1b}\n"
      f"2a = {set2a}\n"
      f"2b = {set2b}\n")

set3a = solve([5*x + 3*y - 9,
               2*x + y - 4],
              x, y, dict=True)
set3b = solve([2*x + y + z - 6,
               x + 3*y + z - 2,
               2*x + y + 2*z - 9],
              x, y, z, dict=True)
set3c = solve([x + y + 3*z + 1,
               3*x + y + z - 5,
               2*x + y + 2*z - 2],
              x, y, z, dict=True)

print(f"Osa 3 yhtälöryhmät:\n"
      f"a = {set3a}\n"
      f"b = {set3b}\n"
      f"c = {set3c}\n")