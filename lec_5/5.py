import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.loadtxt('1.txt')

fig, ax = plt.subplots(1,2)

ax[0].plot(x, np.sin(x), label='sin(x)')
ax[0].plot(y[:,0], y[:,1], label='cos(x)')
ax[0].set_xlabel('Angle in radians')
ax[0].set_ylabel('sin(x)/cos(x)')
ax[0].set_title('sin(x) vs cos(x)') 
ax[0].legend()
ax[1].plot(np.random.rand(30), np.random.rand(30), 'r*')
plt.show()
