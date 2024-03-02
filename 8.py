import numpy as np
from scipy import linalg
vecs = np.array([
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]])
r = 2.5
v = 1
def closest(vecs, v, r):
    k=0
    for i in range(len(vecs)):
        if r>linalg.norm(vecs[i]) and i!=v :
            k=k+1
    return k
print(closest(vecs, v, r))
