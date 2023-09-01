import numpy as np

# T1
t1 = np.random.randint(9, size=5)
print(f"{'T1':-^15}\n"
      f"{t1}\n"
      f"{'':-^15}\n")

# T2
t2_a = np.array([[2, 3], [4, -7]])
t2_b = np.array([[1, 1, 1], [3, -3, 2]])
print(f"{'T2':-^15}\n"
      f"a) {t2_a}\n\n"
      f"b) {t2_b}\n"
      f"{'':-^15}\n")

# T3
print(f"{'T3':-^15}\n"
      f"{'Normit:':<15}")
print(f"{'u':<3} = {np.linalg.norm(t2_a[0]):>8.3f}\n"
      f"{'v':<3} = {np.linalg.norm(t2_a[1]):>8.3f}\n"
      f"{'uu':<3} = {np.linalg.norm(t2_b[0]):>8.3f}\n"
      f"{'vv':<3} = {np.linalg.norm(t2_a[1]):>8.3f}\n")
print(f"{'':-^15}")
