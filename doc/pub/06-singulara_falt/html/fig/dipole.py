# Start initialization
import numpy as np
import pylab as p

# Make an x,z grid
grid = np.linspace(-6,6,200)
x, z = np.meshgrid(grid,grid)
mu=4*np.pi  # dipole strength (in z-direction)
# and the 2D cross section of the potential (scalar field)
phi = mu * z / (4 * np.pi * (x**2+z**2)**(3/2))
# End initialization

# Start contour plot
from matplotlib import colors
p.figure(figsize=(6,6))
heights = np.linspace(-0.6,0.6,7)
CS = p.contour(x,z,phi,heights,colors='k')
p.clabel(CS, inline=1, fontsize=10,fmt='%3.1f')
p.xlabel(r'$x$')
p.ylabel(r'$z$')
# End contour plot

# Start fieldline plot
Fx = mu / (4 * np.pi * (x**2+z**2)**(5/2)) * 2*x*z
Fz = mu / (4 * np.pi * (x**2+z**2)**(5/2)) * (z**2-x**2)
p.streamplot(x,z,Fx,Fz)
# End fieldline plot
CS = p.contour(x,z,phi,heights,colors='k')
p.clabel(CS, inline=1, fontsize=10,fmt='%3.1f')
p.savefig('dipole_fieldplot.png')

#p.show()
