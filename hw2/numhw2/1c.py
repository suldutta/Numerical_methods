import numpy as np
import matplotlib.pyplot as plt

n=21
a=-1
b=1
x0=-1
v_b=[]
v_n=[]
def f(x):
    return(np.sin(np.cos(np.exp(x))))
def g(x):
    return(-(np.sin(np.exp(x)))*(np.cos(np.cos(np.exp(x))))*(np.exp(x)))

for i in range(n):
    t=(a+b)/2.0
    f1=f(a)
    f2=f(b)
    ft=f(t)
    if(f1*ft>0):
        a=t
    elif(f2*ft>0):
        b=t
    v_b.append(t)
    x0=x0-(f(x0)/g(x0))
    v_n.append(x0)

print("Bisection root ",t)
print("Newton Rhapson Root",x0)
error1=[]
error2=[]
x=[]
for i in range(n-1):
    e1=v_b[i+1]-v_b[i]
    error1.append(e1)
    e2=v_n[i+1]-v_n[i]
    error2.append(e2)
    x.append(i)

plt.plot(x,error1,label="Bisection method")
plt.plot(x,error2,label="Newton Rhapson method")
plt.xlabel("Iteration no. --->")
plt.ylabel("Error --->")
plt.legend()
plt.show()
