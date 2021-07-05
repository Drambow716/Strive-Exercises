import numpy as np

a = np.random.random((5,5))
print(a)

a[[0,1]] = a[[1,0]]
print(a)
