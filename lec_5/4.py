import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

z = np.zeros((100,2))
z[:,0] = x[:]
z[:,1] = y[:]
np.savetxt('1.txt', z, delimiter='  ')
