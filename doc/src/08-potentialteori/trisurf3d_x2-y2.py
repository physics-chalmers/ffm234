from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

n_angles = 36
n_radii = 8

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)

# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Amplitudes [c0,cx,cy,cxy,cii]
c=[0,0,0,1,0]

# x^2 - y^2 surface
fig = plt.figure()
ax = fig.gca(projection='3d')
c=[0,0,0,0,1]
z = c[0]+c[1]*x+c[2]*y+c[3]*x*y+c[4]*x**2 -c[4]*y**2
ax.plot_trisurf(x, y, z, cmap=cm.cubehelix, linewidth=0.2)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$x^2-y^2$')
fig.savefig('x2y2.png')

#xy surface
x=np.linspace(0,1,10,endpoint=True)
y=np.linspace(0,1,10,endpoint=True)
xx, yy = np.meshgrid(x, y)
x=xx.flatten()
y=yy.flatten()

c=[0,0,0,1,0]
z = c[0]+c[1]*x+c[2]*y+c[3]*x*y+c[4]*x**2 -c[4]*y**2

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, cmap=cm.cubehelix, linewidth=0.2)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$xy$')
fig.savefig('xy.png')

