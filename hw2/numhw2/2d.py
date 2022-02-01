from scipy import integrate
import numpy as np

def f(x):
    return(np.exp(x))

x=np.arange(0,1,0.01)
sum1=integrate.simps(f(x),x)
print("Using Simpson",sum1)

sum2=integrate.fixed_quad(f,0.0,1.0,n=5)
print("Using 5th order Gaussian quadrature ",sum2)

sum3=np.trapz(f(x),x)
print("using trapezoidal ",sum3)

sum4=integrate.romberg(f,0,1)
print("using romberg ",sum4)
