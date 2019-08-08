# Start initialization
import numpy as np
import pylab as p

# Make an x,y grid
grid = np.linspace(-10000,10000,500)
x, y = np.meshgrid(grid,grid)
# and the 2D field
R0=4000  # radius measure
h0= 2106 # peak height
h = h0 / (1 + (x**2 + y**2)/R0**2)
# End initialization

# Start surface plot
from mpl_toolkits.mplot3d import Axes3D
fig = p.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x/1000, y/1000, h)
#ax.set_zlim3d(-1, 1)
ax.set_xlabel(r'$x$ (km)')
ax.set_ylabel(r'$y$ (km)')
ax.set_zlabel(r'$h$ (m)')
# End surface plot
p.savefig('hojd_surface.png')

# Start contour plot
from matplotlib import colors
p.figure(figsize=(6,6))
heights = np.linspace(500,2000,4)
CS = p.contour(x/1000,y/1000,h,heights,colors='k')
p.clabel(CS, inline=1, fontsize=10)
p.xlabel(r'$x$ (km)')
p.ylabel(r'$y$ (km)')
# End contour plot
p.savefig('hojd_contour.png')
# Start colormesh plot
p.pcolormesh(x/1000, y/1000, h, cmap=p.get_cmap('cubehelix_r'))
# End colormesh plot
p.savefig('hojd_contour_colormesh.png')

# Start gradient plot
p.figure(figsize=(6,6))
grid_course =  np.linspace(-10000,10000,11)
x_c, y_c = np.meshgrid(grid_course,grid_course)
radius = 2000
outside = x_c**2 + y_c**2 > radius**2
gradh_x = - 2*h0 / (R0**2 * (1 + (x_c**2+y_c**2)/R0**2)**2) * x_c
gradh_y = - 2*h0 / (R0**2 * (1 + (x_c**2+y_c**2)/R0**2)**2) * y_c
p.quiver(x_c[outside]/1000,y_c[outside]/1000,gradh_x[outside],gradh_y[outside],scale=3)
p.xlabel(r'$x$ (km)')
p.ylabel(r'$y$ (km)')
# End gradient plot
p.savefig('hojd_gradient.png')

#p.show()
