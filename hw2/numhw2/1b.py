import numpy as np
def f(x):
    return np.sin(np.cos(np.exp(x)))
def g(x):
    return -np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x))
def newtonRhap(x0):
    h=f(x0)/g(x0)
    while(abs(h)>=0.0001):
        h=f(x0)/g(x0)
        x0=x0-h
    print("Root by Rhapson method is ",x0)     

x0=-1
newtonRhap(x0)
