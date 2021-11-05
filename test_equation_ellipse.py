import numpy as np
from matplotlib import pyplot as plt
import random

fig = plt.figure()
fig.set_dpi(100) #résolution de la figure
fig.set_size_inches(7, 6.5)



ax = plt.gca() #récup axe x
ax.set_xlim(-10, 10)
ax.set_ylim(-10,10)

t = np.linspace(0, 2*np.pi, 100)
print(t)



for i in range(100):
    a = random.uniform(4, 7)
    b = random.uniform(4, 7)
    x = 0 + a*np.cos(t)
    y = 0 + b*np.sin(t)
    plt.plot(x, y)

plt.scatter(3, 0, c = 'orange')

plt.show()