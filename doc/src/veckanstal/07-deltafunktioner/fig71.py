# Start initialization
import numpy as np
import scipy.special as scisp
import pylab as p

def Hlorentz(x,eps):
    return 0.5+np.tanh(x/eps)/2

def Hgauss(x,eps):
    return 0.5+scisp.erf(x/eps)/2

# Make an x grid
x = np.linspace(-3,3,500)
# End initialization

# Start  plot
p.figure(figsize=(6,6))
ax=p.gca()
for eps in [0.02,0.1,0.5]:
    ax.plot(x,Hlorentz(x,eps),label=r'$\epsilon=%4.2f$' %eps)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$H_\epsilon(x)$')
ax.set_ylim([-.09,1.09])
p.legend(loc='best')
ax.set_title('Lorentziansk approximation')
# End plot
p.savefig('Hlorentz.png')

# Start  plot
p.figure(figsize=(6,6))
ax=p.gca()
for eps in [0.02,0.1,0.5]:
    ax.plot(x,Hgauss(x,eps),label=r'$\epsilon=%4.2f$' %eps)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$H_\epsilon(x)$')
ax.set_ylim([-.09,1.09])
p.legend(loc='best')
ax.set_title('Gaussisk approximation')
# End plot
p.savefig('Hgauss.png')

#p.show()
