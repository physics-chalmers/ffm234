import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def E(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = ((x-r0[0])**2 + (y-r0[1])**2)**1.5
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

def Phi(q, r0, x, y):
    """Return the electric potential due to charge q at r0."""
    den = np.sqrt((x-r0[0])**2 + (y-r0[1])**2)
    return q / den

# Grid of x, y points
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

# We will consider three cases: single, dirichlet, neumann
# corresponding to: single charge, two opposite charges, two equal charges,
# respectively
cases = {}

# Start with a single charge, q=+1, at x=0, y=1
charges = [(1,(0,1))]
cases['single'] = charges

# Create a mirror system with 2 charges of opposite sign
charges = [(1,(0,1)),(-1,(0,-1))]
cases['dirichlet'] = charges

# Create a mirror system with 2 charges of equal sign
charges = [(1,(0,1)),(1,(0,-1))]
cases['neumann'] = charges

# Contour levels
levels = [-10, -2, -1, -0.5, -0.1, 0, 0.1, 0.5, 1, 2, 10]

for case, charges in cases.items():

    # Electric field vector, E=(Ex, Ey), as separate components
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    # Electric potential
    Phitot = np.zeros((ny, nx))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey
        Phitot += Phi(*charge, x=X, y=Y)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot the streamlines with an appropriate colormap and arrow style
    color = np.log(np.sqrt(Ex**2 + Ey**2))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                  density=1, arrowstyle='->', arrowsize=1.5)

    # Plot the contours, negative ones will be dashed
    CS = ax.contour(x, y, Phitot, levels,
                 colors='k',  # negative contours will be dashed by default
                 )
    ax.clabel(CS, fontsize=9, inline=1)


    # Add filled circles for the charges themselves
    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect('equal')

    plt.savefig('fieldplot_%s.png' %case,bbox_tight=True)

plt.show()
