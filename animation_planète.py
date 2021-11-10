import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


terre = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_Terre.csv', delimiter = ',', dtype = None)
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


fig, ax = plt.subplots(1, 1)
ax = plt.gca()

ax.set_facecolor((0, 0, 0))





plt.xlim([4000, 6000])
plt.ylim([4000, 6000])
terre, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
jupiter, = plt.plot([], [], 'ko', ms = 4, mfc = 'yellow')

def animate(i):
    terre.set_data(x[i], y[i])
    jupiter.set_data(a[i], b[i])
    return terre, jupiter,



anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 20, blit = True, repeat = True)

#ax.patch.set_facecolor

plt.show()