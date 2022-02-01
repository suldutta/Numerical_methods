
import numpy as np
from scipy import optimize
def f(x):
    return np.sin(np.cos(np.exp(x)))
root1=optimize.bisect(f,-1,1)
root2=optimize.newton(f,1.0)
print("Root from bisection method :",root1)
print("Root using Newton Rhapson :",root2)

