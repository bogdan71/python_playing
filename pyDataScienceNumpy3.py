import numpy as np

def makeTwoDim(x):
    if len(x.shape)==1:
        x = x.reshape(len(x) // 2, 2)
    return x

# apple stock prices (May 2018)
prices = [189, 186, 186, 188,
          187, 188, 188, 186,
          188, 188, 187, 186]
data = np.array(prices)
data = makeTwoDim(data)
print(np.average(data[-1]))

Solution
186.5

Explanation
Numpy is a popular Python library for data science focusing on linear algebra.

This advanced puzzle combines multiple language concepts and numpy features. The topic is a miniature stock analysis of the Apple stock.

The puzzle creates a one-dimensional numpy array from raw price data. Note that the shape property of an n-dimensional numpy array is a tuple with n elements. Thus, a one-dimensional numpy array has a shape property of length one.

The function makeTwoDim(x) uses this to detect one-dimensional numpy arrays. Then, it transforms these into two-dimensional arrays using the reshape function. For each of the two dimensions, the reshape function needs the number of elements of this dimension. In particular, it creates a numpy array with two columns and half the number of rows.

Finally, we access the last row of this numpy array that contains the two numbers 187 and 186 and average them.