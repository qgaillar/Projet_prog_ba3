import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100) #résolution de la figure
fig.set_size_inches(7, 6.5) #def de la figur en pouces

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((2, -2), 0.2, fc='y')

def init():
    patch.center = (u, v)
    ax.add_patch(patch)
    return patch,

def animate(t):
    x, y = patch.center
    x = u + a * np.cos(t)
    y = v + b * np.sin(t)
    patch.center = (x, y)
    return patch,
u = 5
v = 5
a = 2
b = 1.5
t = np.linspace(0, 2*np.pi, 500)
anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=200,
                               blit=True)

plt.show()