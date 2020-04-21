import numpy as np

v = np.array([3, 7])
u = np.array([2, 2])
print(v + u)
v = np.array([3, 7])
print(2 * v)

v = np.array([3, 7])
u = np.array([2, 2])
print(v.dot(u))

v = np.array([3, 2, 7])
print(np.linalg.norm(v))

def unit_vector(v):
    return v / np.linalg.norm(v)
u = np.array([3, 6, 4])
print(unit_vector(u))