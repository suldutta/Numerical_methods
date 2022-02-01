import numpy as np 

def f(x):
    return(np.exp(x))

def left(f,n):
    a=0.0
    b=1.0
    deltax=(b-a)/n
    sum1=0.0
    x=a
    for i in range(1,n+1):
        x=a+(i-1)*deltax
        sum1=sum1+f(x)*deltax
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

print("using leftpoint",left(f,100))
print("using rightpoint", right(f,100))
print("using midpoint", mid(f,100))

S=np.exp(1)-1
print(S)
err1=np.abs(S-left(f,100))
err2=np.abs(S-right(f,100))
err3=np.abs(S-mid(f,100))
flag=0
if(err1<err3):
    if(err1<err2):
        flag=1
    else:
        flag=3
else:
    if(err3<err2):
        flag=2
    else:
        flag=3

if(flag==1):
    print("Left point method is better")
elif(flag==2):
    print("Mid point method is better")
elif(flag==3):
    print("Right point method is better")




