import sys
import numpy as np
import matplotlib.pyplot as plt

w = 3
Z, X = np.mgrid[-w:w:150j, -w:w:150j]
R = np.sqrt(X**2+Z**2)

U = 3*Z*X / R**5
W = (2*Z**2 - X**2) / R**5 

fig = plt.figure()
ax = fig.add_subplot(111)

strm = ax.streamplot(X, Z, U, W, linewidth=2)

ax.set_title(r'Streamplot, dipole field $\vec{E} = \frac{\mu}{4\pi r^3} \left( 2\cos\theta\hat r + \sin\theta\hat\theta \right)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$z$')

ax.set_aspect('equal')

#plt.show()
plt.savefig('efield-dipole.png')
