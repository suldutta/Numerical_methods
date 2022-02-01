import numpy as np
def f(x):
        return np.sin(np.cos(np.exp(x)))
a=-1.0

b=1.0

n=100
t=0
if(f(a)*f(b)>=0):
        print("wrong guess")
for i in range(1,n):
        t=(a+b)/2.0
        if(f(a)*f(t)<0):
           a=a
           b=t
        elif(f(b)*f(t)<0):    
           b=b
           a=t
        elif(f(t)==0):    
           print("Root in bisection method is",t)
           break
        else:    
           print("Bisection method fails")
           break
print("root is: ",t)        
