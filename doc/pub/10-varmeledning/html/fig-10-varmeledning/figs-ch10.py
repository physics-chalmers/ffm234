# Start initialization
import numpy as np
import pylab as p

# Greens function D=1
def G(x,t):
    if t<0:
        g = np.zeros(len(x))
        return g
    else:
        return np.exp(-x**2/(4*t)) / (np.sqrt(4*np.pi*t)) 
    
# End initialization

# Start plot 1
x=np.linspace(-1,1,200)
p.figure(figsize=(6,6))
for t in [-1,.001,0.005,0.01,0.05,0.1]:
    p.plot(x,G(x,t))
p.xlabel(r'$x$')
p.ylabel(r'$G(x,t)$')
# p.ylim([-1,6])
# End plot 1
p.savefig('greens_function_1dim_wtime.png')

