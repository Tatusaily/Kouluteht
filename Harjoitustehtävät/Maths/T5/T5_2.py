from sympy import *
from sympy.abc import x, y, z

print(f"{'2.':-<16}")

print(f"{'1)':.<16}")
print(f"{'Transpoosit':-<16}")
m_1_a = Matrix([[4, 9, 0], [-3, 7, -11]])
m_1_b = Matrix([[8, 9], [-3, -12], [0, -1], [7, 1]])
print("a)")
pprint(m_1_a.T)
print("b)")
pprint(m_1_b.T)
print(f"{'':-<16}")


print(f"{'2)':.<16}")
print(f"{'Determinaatit':-<16}")

print("a)")
m_2_a = Matrix([[5, -6], [8, 10]])
print(m_2_a.det())

print("b)")
m_2_b = Matrix([[1-x, -x], [x, 1-x]])
pprint(m_2_b.det())

print("c)")
m_2_c = Matrix([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
pprint(m_2_c.det())

print("d)")
m_2_d = Matrix([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
pprint(m_2_d.det())


print(f"{'3)':.<16}")
print(f"{'Determinaatti:':-<16}")
m_3 = Matrix([[-2, 0, 8, 5],
              [3, -1, 2, 1],
              [4, 7, 6, 2],
              [1, 0, 2, 3]])
pprint(m_3.det())
