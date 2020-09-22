import numpy as np

x = np.array([[1, 3, 5],
              [1, 1, 1],
              [0, 2, 4]])

y = np.average(x, axis=1)
print(y[0])
print(y[1])
print(y[2])