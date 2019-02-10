import pygame
import numpy as np

class A(object):
    def __init__(self):
        self.a = np.ones((2, 3))

    def __getitem__(self, i):
        return self.a[i]

a = A()
print(a[0, 1])
def a(u, v):
    print(u, v)

b = {"u": 3, "v": 6}
a(**b)
