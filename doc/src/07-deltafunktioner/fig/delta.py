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

# Start plot
x=np.linspace(-1,1,200)
for case in range(4):
    p.figure(figsize=(6,6))
    for eps in np.linspace(0.5,0.1,5):
        p.plot(x,h(eps,x,case))
    p.xlabel(r'$x$')
    p.ylabel(r'$h_{%i,\epsilon}(x)$' %case)
    # End plot
    p.savefig('delta%i.png' %case)

