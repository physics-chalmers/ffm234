# Start initialization
import numpy as np
import pylab as p

# Make an x,y grid
grid = np.linspace(-3,3,500)
x, y = np.meshgrid(grid,grid)
# and the 2D field
A=1  # radius measure
phi = A * (x**2 - y**2)/2
# End initialization

# Start contour plot
from matplotlib import colors
p.figure(figsize=(6,6))
ax=p.gca()
#heights = np.linspace(500,2000,4)
CS = ax.contour(x,y,phi,colors='k')
ax.clabel(CS, inline=1, fontsize=10)
ax.set_xlabel(r'$x$ (au)')
ax.set_ylabel(r'$y$ (au)')
# End contour plot
# p.savefig('stagnation_phi.png')

grid_course =  np.linspace(-3,3,11)
x_c, y_c = np.meshgrid(grid_course,grid_course)
radius = 0.5
outside = x_c**2 + y_c**2 > radius**2
gradh_x = - A * x_c
gradh_y = A * y_c

# Start streamplot 
# p.figure(figsize=(6,6))
ax.streamplot(grid_course,grid_course,gradh_x,gradh_y,density=0.8)
#p.xlabel(r'$x$ (au)')
#p.ylabel(r'$y$ (au)')
# End streamplot
#p.savefig('stagnation_stream.png')
p.savefig('stagnation_fieldplot.png')

#p.show()
