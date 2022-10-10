from telnetlib import OLD_ENVIRON
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from math import tanh

# first car - speed distance time v = 5 t = 0


#dxi/dt = vi
#dvi/dt = a [V(xi+1-xi)-vi],
#position for first car


def model(v,t):
    return v

def model2(v2,t,y2,y1,v1):
    # Car1
    y1 = v1 * t

    # Car2
    sens = 0.1
    a = sens * float(V(y1 - y2)) - v2
    v2 += a
    return v2

def V(b):
    return float(tanh(b-2) + tanh(2))

v1 = 1.0
v2 = 5.0

y1 = 100.0
y2 = 0.0

t = np.linspace(0,1000)

#y1 = odeint(model,v1,t)
car1 = odeint(model,v1,t)
car2 = odeint(model2,v2,t, args=(y2,y1,v1,))


plt.plot(t,car2)
#plt.plot(car2,t)
plt.show()