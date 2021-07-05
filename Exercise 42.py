import numpy as np
x = np.random.randint(0,2,6)
print("First array:")
print(x)
y = np.random.randint(0,2,6)
print("Second array:")
print(y)
array_equal = np.allclose(x, y)
if array_equal == False:
    print("No they are not Equal")
else:
    print("Ouraa, They are Equal")
