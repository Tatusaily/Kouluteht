from sympy import *

print(f"{'1.':-<16}")
print(f"{'Kertolaskut':-<16}")

print(f"{'a)':.<16}")
m_a1 = Matrix([[-1, 2], [3, 1]])
m_a2 = Matrix([[0, 1, 3], [2, -3, 5]])
pprint(m_a1)
pprint(m_a2)
pprint(m_a1*m_a2)

print(f"{'b)':.<16}")
m_b1 = Matrix([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
m_b2 = Matrix([1, -3, -1])
pprint(m_b1)
pprint(m_b2)
pprint(m_b1*m_b2)

print(f"{'c)':.<16}")
m_c1 = Matrix([[2, 0, 1], [1, -3, 4], [0, -1, 5]])
m_c2 = Matrix([3, -5, -7])
pprint(m_c1)
pprint(m_c2)
pprint(m_c1*m_c2)

print(f"{'d)':.<16}")
m_d1 = Matrix([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
m_d2 = Matrix([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
pprint(m_d1)
pprint(m_d2)
pprint(m_d1*m_d2)

print(f"{'':-<16}")
