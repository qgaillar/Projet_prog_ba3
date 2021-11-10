import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


planète = np.genfromtxt('/Users/quentingaillard/Downloads/planete_test (2).csv', delimiter = ',', dtype = None)
print(planète[0,0])

x = planète[:, 0]
y = planète[:, 1]



x_min = 1000
x_max = 4000

y_min = 1000
y_max = 4000


fig = plt.figure()
ax = plt.axes(xlim=(0, x_max), ylim=(0, y_max))
patch = plt.Circle((2, -2), 50, fc='green')

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
    
plt.scatter(1998.5, 2000, s= 10, c =  'y', alpha = 1)
ani = animation.FuncAnimation(fig, animate,init_func= init, frames = 100, blit = True, interval = 20, repeat = True)

plt.show()





#plt.plot(x, y)
#plt.show()

