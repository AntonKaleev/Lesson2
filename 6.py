import numpy as np
def nonzero(A):
    for i in range(100):
        for j in range(100):
            if A[i][j]!=0:
                x=i
                y=j
    return x, y
A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))
#7
masiv = np.array([3, 2, 5, 4, 1, 7])
min=masiv.min()
c=2
for j in range(3):
    index = np.argmin(masiv)
    print(index)
    masiv[index]=masiv.max()

