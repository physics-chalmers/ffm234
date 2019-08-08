# Start initialization
import numpy as np
import pylab as p

# Delta function approximation 1 - 4
def h(eps,x,case):
    if case==0:
        h = np.zeros(len(x))
        h [abs(x) < eps] = 1/eps
        return h
    elif case==1:
        return np.exp(-x**2/eps**2) / (np.sqrt(np.pi)*eps)
    elif case==2:
        return eps / (np.pi * (x**2 + eps**2))
    elif case==3:
        return np.sin(x/eps) / (np.sqrt(np.pi)*x)
    
# End initialization

# Start plot 1
x=np.linspace(-1,1,200)
p.figure(figsize=(6,6))
eps = 0.2
p.plot(x,h(eps,x,0))
p.xlabel(r'$x$')
p.ylabel(r'$h_{\epsilon}(x)$')
p.ylim([-1,6])
# End plot 1
p.savefig('delta_step.png')

# Start plot 2
x=np.linspace(-1,1,200)
p.figure(figsize=(6,6))
p.plot(x,-abs(x)/2)
p.plot(x,np.zeros(len(x)),'k')
p.xlabel(r'$x$')
p.ylabel(r'$\phi(x) [q]$')
p.ylim([-0.6,0.1])
# End plot 2
p.savefig('pointcharge_pot_1dim.png')

# Start plot 3
x=np.linspace(-1,1,200)
p.figure(figsize=(6,6))
p.plot(x,np.sign(x)/2)
p.plot(x,np.zeros(len(x)),'k')
p.xlabel(r'$x$')
p.ylabel(r'$F(x) [q]$')
# End plot 3
p.savefig('pointcharge_field_1dim.png')
