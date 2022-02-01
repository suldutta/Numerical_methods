import numpy as np

def f(x):
    return(np.exp(x))

def trapezoidal(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    s1=f(a)+f(b)
    x=a
    for i in range(1,n):
        x=a+i*h
        s1=s1+2*f(x)
    s1=s1*(h/2)
    return(s1)

def simpson(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    s2=f(a)+f(b)
    x=a+h
    for i in range(1,int(n/3)):
        s2=s2+4*f(x)
        x=x+2*h
    s2=s2*(h/3)
    return(s2)

print("using trapezoidal ",trapezoidal(f,100))
print("using simpson's method ",simpson(f,100))
