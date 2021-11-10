import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)



fig = plt.figure()
fig.set_dpi(100) #résolution de la figure
fig.set_size_inches(7, 6.5) #def de la figure en pouces, jsp pourquoi mais c'est moins clean quan dil n'y pas cette ligne

ax = plt.axes(xlim=(0, 10000), ylim=(0, 10000))
patch = plt.Circle((2, -2), 200, fc='y')

def init():
    patch.center = (2, 2)
    ax.add_patch(patch)
    return patch,

def animate(i): 
    t = i * dt
    y = np.cos(k*x - w*t)
    patch.center = (x, y)
    return patch,
    
 
ani = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval=20, repeat=False)

plt.show()