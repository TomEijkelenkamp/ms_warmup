from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def model(t):
    k = 0.5
    dxdt= k/t
    return dxdt

x = [5]
t = np.linspace(1,20,100)

y = odeint(model,t)

fig,ax = plt.subplots()
ax.plot(t,y)
plt.show()