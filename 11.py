import matplotlib.pyplot as plt
import numpy as np
y = np.random.standard_cauchy(10**6)
plt.hist(y,range=(0, 5),bins=50,density=True)
#plt.hist(y)
plt.show()