import re

import numpy as np


def getString(fn):
    f = open(fn, 'r')
    myString = f.read()
    return myString.lower()


def getIncidence(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    Nc = len(letters)
    n = np.zeros(Nc, dtype=np.float64)  # Creates an array with all 0s with the size 26
    i = 0
    for c in letters:
        xx = re.findall(c, string)
        n[i] = len(xx) * 1.0
        i += 1
    return n


def compute_frequency():
    z = np.array([])
    c = np.bincount(z)
    ii = np.nonzero(c)[0]

    return ii


x = np.array([1., 4., 2., 6.5, .4, 65., 4., 34.])
y = compute_frequency()
print(y)
