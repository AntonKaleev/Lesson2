import numpy as np
#1
matrix = np.array([[1]*2]*2)
print(matrix)
#2
a = [1, 2, 3]
b = np.array([1, 2, 3])
print(a + a, b + b)
#3
a = [1, 2, 3, 4, 5, 6]
b = [10, 11, 12, 13, 14, 15]
x = np.min((np.max(a), np.min(b)))
print(x)
#4
A = np.array([[10, 1], [20, 2]])
x = np.sum(A, axis = 0)
print(x)
#5
I = np.eye(2)
A = np.array([[0, 1], [1, 0]])
x = np.sum( np.dot(A, I) )
y = np.sum( A * I )
print(x, y)

