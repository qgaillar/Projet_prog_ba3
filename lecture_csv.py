import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


planète = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_test.csv', delimiter = ',', dtype = None)
print(planète[0,0])

x = planète[:, 0]
y = planète[:, 1]



x_min = 0
x_max = 10000

y_min = 0
y_max = 10000


fig = plt.figure()
ax = plt.axes(xlim=(0, 10000), ylim=(0, 10000))
patch = plt.Circle((2, -2), 200, fc='y')

def init():
    patch.center = (2, 2)
    ax.add_patch(patch)
    return patch,


def animate(i):
    coord_x, coord_y = patch.center
    coord_y = y[i]
    coord_x = x[i]
    print(coord_y)
    patch.center = (coord_x, coord_y)
    return patch,
    

ani = animation.FuncAnimation(fig, animate,init_func= init, frames = 360, blit = True, interval = 20, repeat = True)

plt.show()





#plt.plot(x, y)
#plt.show()

