# Start initialization
import numpy as np
import pylab as p

# Make an x,y grid
grid = np.linspace(-4,4,100)
x, y = np.meshgrid(grid,grid)
# and the 2D fields
xi = x**2 - y**2
eta = x * y
# End initialization

# Start contour plot
p.figure(figsize=(6,6))
CS = p.contour(x,y,xi,5,colors='k')
p.clabel(CS, inline=1, fontsize=10)
p.text(0.5,1.3,r'$\xi$-yta',color='k',rotation=45)
CS = p.contour(x,y,eta,5,colors='r')
p.clabel(CS, inline=1, fontsize=10)
p.text(1,0.05,r'$\eta$-yta',color='r')
p.xlabel(r'$x$')
p.ylabel(r'$y$')
# End contour plot
p.savefig('koordinatytor.png')

#p.show()
