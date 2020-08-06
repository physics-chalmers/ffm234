### Start initialization
import sys
import numpy as np
import matplotlib.pyplot as plt
### End initialization
### Start Alt2: Streamlines with streamplot ###
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
R = np.sqrt(X**2+Y**2)
U = -Y / R**2 # Note that -Y/R = -sin(phi)
V = X / R**2  # Note that X/R = cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111)

strm = ax.streamplot(X, Y, U, V, linewidth=2)

ax.set_title(r'Streamplot, vortex field ' +\
        r'$\vec{F} = \frac{J}{2\pi\rho}\hat\varphi$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

ax.set_aspect('equal')

plt.savefig('streamlines-vortex.png')
### End Alt2

### Start Alt1: Streamlines as 2d curves ###
def curve(rho0,x):
    """Fieldline for vortex streamlines in Cartesian coordinates.
    Assume z=0 => Fieldline in xy-plane.
    We also avoid the singularity at x=y=0."""
    if max(abs(x)) > rho0:
        print('Fieldline for rho_0=%3.1f is only defined for |x| <= %3.1f' %(rho0,rho0))
        return None
    return np.sqrt(rho0**2 - x**2)

fig = plt.figure()
ax = fig.add_subplot(111)

# Grid of x points
nx = 64

# Streamline constant
for rho0 in np.linspace(1,3,5):

    # Grid of x points
    x = np.linspace(-rho0,rho0, nx)

    yp = curve(rho0,x)
    ym = -curve(rho0,x)

    # Plot the streamlines with an appropriate colormap and arrow style
    ax.plot(x, yp, 'b-', x, ym, 'b-', linewidth=2)
    ax.annotate("", xy=(max(x), 0.1), xytext=(max(x), 0), arrowprops=dict(arrowstyle="->",color='b'))

ax.set_title(r'Streamplot, vortex field $\vec{F} = \frac{J}{2\pi\rho}\hat\varphi$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

ax.set_aspect('equal')
### End Alt1

#plt.show()
plt.savefig('streamlines-vortex-curves.png')
