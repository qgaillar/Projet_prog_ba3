import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100) #résolution de la figure
fig.set_size_inches(7, 6.5) #def de la figure en pouces, jsp pourquoi mais c'est moins clean quan dil n'y pas cette ligne

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((2, -2), 0.2, fc='y')

def init():
    patch.center = (2, 2)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.cos(np.radians(i))
    y = 5 + 2.5 * np.sin(np.radians(i))
    patch.center = (x, y)
    return patch,

u = 5
v = 5
a = 3
b = 2.5
t = np.linspace(0, 2*np.pi, 10000)
plt.plot( u + a * np.cos(t), v + b * np.sin(t))
plt.grid(color = 'lightgray', linestyle = '--')




anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=10,
                               blit=True)

plt.show()
