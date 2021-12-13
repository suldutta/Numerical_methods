import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.loadtxt('1.txt')

plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(y[:,0], y[:,1], label='cos(x)')
plt.xlabel('Angle in radians')
plt.ylabel('sin(x)/cos(x)')
plt.title('sin(x) vs cos(x)') 
plt.legend()
plt.show()
