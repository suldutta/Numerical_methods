import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return(np.exp(x))

def left(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    sum1=0.0
    x=a
    for i in range(1,n+1):
        x=a+(i-1)*h
        sum1=sum1+f(x)*h
    return(sum1)

def right(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    sum2=0.0
    x=a
    for i in range(1,n+1):
        x=a+i*h
        sum2=sum2+f(x)*h
    return(sum2)

def mid(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    sum3=0.0
    x=a
    for i in range(1,n+1):
        x=a+(i-0.5)*h
        sum3=sum3+f(x)*h
    return(sum3)

def trapezoidal(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    sum4=f(a)+f(b)
    x=a
    for i in range(1,n):
        x=a+i*h
        sum4=sum4+2*f(x)
    sum4=sum4*(h/2)
    return(sum4)

def simpson(f,n):
    a=0.0
    b=1.0
    h=(b-a)/n
    sum5=f(a)+f(b)
    x=a+h
    for i in range(1,int(n/3)):
        sum5=sum5+4*f(x)
        x=x+2*h
    x=a+2*h
    for j in range(1,int(n/2)):
        sum5=sum5+2*f(x)
        x=x+2*h
    sum5=sum5*(h/3)
    return(sum5)

def error(g):
    integral=np.zeros(100)
    err=np.zeros(99)
    n=100
    for j in range(1,n+1):
        integral[j-1]=g(f,j)
    for k in range(1,n):
        err[k-1]=integral[k]-integral[k-1]
    return(err)

integral=np.zeros(50)
errSimp=np.zeros(49)

for j in range(1,51):
    integral[j-1]=simpson(f,2*j)
for k in range(1,50):
    errSimp[k-1]=integral[k]-integral[k-1]

n=np.linspace(2,100,99)
n_Sim=np.linspace(2,100,49)

plt.plot(n,error(left),label="using leftpoint")
plt.plot(n,error(right),label="using rightpoint")
plt.plot(n,error(mid),label="using midpoint")
plt.plot(n,error(trapezoidal),label="using trapezoidal")
plt.plot(n_Sim,errSimp,label="using simpson")

plt.xlabel("No. of iterations --->")
plt.ylabel("Error --->")

plt.legend()
plt.show()

