# Start initialization
import numpy as np
import pylab as p

# Make an x,z grid
grid = np.linspace(-6,6,201)
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
p.clabel(CS, inline=1, fontsize=10)
p.xlabel(r'$x$')
p.ylabel(r'$z$')
# End contour plot
p.savefig('dipole.png')

# Start gradient plot
#--p.figure(figsize=(6,6))
#--grid_course =  np.linspace(-10000,10000,11)
#--x_c, y_c = np.meshgrid(grid_course,grid_course)
#--radius = 2000
#--outside = x_c**2 + y_c**2 > radius**2
#--gradh_x = - 2*h0 / (R0**2 * (1 + (x_c**2+y_c**2)/R0**2)**2) * x_c
#--gradh_y = - 2*h0 / (R0**2 * (1 + (x_c**2+y_c**2)/R0**2)**2) * y_c
#--p.quiver(x_c[outside]/1000,y_c[outside]/1000,gradh_x[outside],gradh_y[outside],scale=3)
#--p.xlabel(r'$x$ (km)')
#--p.ylabel(r'$y$ (km)')
#--# End gradient plot
#--p.savefig('hojd_gradient.png')

#p.show()
