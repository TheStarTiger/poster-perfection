import math
import numpy as np
from operator import itemgetter

a = BODY = [0, 0, 0.01, 0.00000004, 0.000002, 0.00000001, 0.00000001, -90000/(90000) +
                             0.0000001, -3, -2, -1, 4, 0, -50, 0]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

c = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])
d = np.array([[1, 2, 3, 5]])
g = [5, 4, 3, 1]

e = np.array([[1, 2, 3], [3, 4, 5], [12, 18, 22]])


def sigmoid(x):
    return 1/(1 + math.exp(-x))

def rough_rgb_hex(hex_str):
    final_rgb = []
    r = int(hex_str[0:2], 16)
    g = int
    return [int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:], 16)]




print(rgb2hex(12, 42, 47))
