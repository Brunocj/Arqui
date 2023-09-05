import numpy as np
import time
import statistics
import matplotlib.pyplot as plt
import ctypes

def cos(x,N):
    cos = 0
    for i in range(0,N):
        fact = 1
        for j in range(1,2*i+1 ):
            fact = fact*j
        cos = cos + ((-1)**i)*(x**(2*i))/fact
    return cos

def py_fast_cos(x, n_terms):
    res = 0
    tn = 1
    for n in range(n_terms):
        res = res + tn
        tn = (-1)*tn*(x**2)/((2*n + 1)*(2*n + 2))
    return res

print(cos(2,1000))
