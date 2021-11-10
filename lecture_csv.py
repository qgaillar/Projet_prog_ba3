import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


terre = np.genfromtxt('/Users/quentingaillard/Downloads/planete_test (2).csv', delimiter = ',', dtype = None)
jupiter = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_Jupiter.csv', delimiter = ',', dtype = None)
print(terre[0,0])

x = terre[:, 0]
y = terre[:, 1]

a = jupiter[:, 0]
b = jupiter[:, 1]



x_min = 1000
x_max = 4000

y_min = 1000
y_max = 4000


fig = plt.figure()
ax = plt.axes(xlim=(0, x_max), ylim=(0, y_max))
terre = plt.Circle((2, -2), 10, fc = 'blue')
jupiter = plt.Circle((2, -2), 100, fc = 'green')

def init():
    terre.center = (2, 2)
    jupiter.center = (1, 1)
    ax.add_patch(terre)
    ax.add_patch(jupiter) 
    return terre, jupiter


def animate(i):
    terre_x, terre_y = terre.center
    jupiter_x, jupiter_y = jupiter.center
    terre_y = y[i]
    terre_x = x[i]
    jupiter_x = a[i]
    jupiter_y = b[i]
    print(jupiter_y)
    terre.center = (terre_x, terre_y)
    jupiter.center = (jupiter_x, jupiter_y)
    return terre, jupiter

r = 2

plt.scatter(1998.5, 2000, s= np.pi * r**2, c =  'y', alpha = 1)
ani = animation.FuncAnimation(fig, animate,init_func= init, frames = 100, blit = True, interval = 20, repeat = True)

plt.show()





#plt.plot(x, y)
#plt.show()
