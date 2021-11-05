import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151



fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 
plt.xlim(0, 10)
plt.ylim(0, 10)

def animate(i): 
    x = 5 + 3 * np.cos(np.radians(i))
    y = 5 + 2.5 * np.sin(np.radians(i))
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, frames=360, blit=True, interval=20, repeat=True)

plt.show()