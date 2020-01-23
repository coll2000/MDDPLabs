import numpy as np
import math


def length(x):
    x = np.array([])
    return math.sqrt(x.dot(x))


def is_parallel(x):
    x = np.array([])
    if x.size != 0:  # If the size is 0, it is a null vector.
        xu = x.math.sqrt(x.dot(x))  # The unit vector of x
        return xu
    else:
        print("NULL VECTOR DETECTED")


a = np.array([1, 2, 3])

print(a)
print(a[0])

# CHECKPOINT 1 --> Print out the second element.
print(a[1])

print(a.dtype.name)

b = np.array([1.5, 2.1, 3.9])
print(b.dtype.name)

print(a.T)

# NumPy - Operations

c = np.array([1., 2.])
d = np.array([2., 1.])

print("Operations: ")

print(2. * c)
print(-.123 * d)
print(c + d)
print(c - d)

u = c.copy()
print(u)

o = np.array([3., -1.5])

print("The dot product of c and o is: ", c.dot(o))
print()
