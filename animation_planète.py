import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planètes import *




terre = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_Terre.csv', delimiter = ',', dtype = None)
jupiter = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_Jupiter.csv', delimiter = ',', dtype = None)
print(terre[0,0])

x_terre = terre[:, 0]
y_terre = terre[:, 1]

x_jupiter = jupiter[:, 0]
y_jupiter = jupiter[:, 1]



x_min, x_max = 4000, 6000
y_min, y_max = 4000, 6000


fig, ax = plt.subplots(1, 1) #définiton de notre figure composé de seulement une ligne et une colonne
ax = plt.gca() #prendre en compte les axes actuels

ax.set_facecolor((0, 0, 0))  #fond de notre plot en noir


plt.xlim([x_min, x_max])
plt.ylim([y_min, y_max])
terre, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
jupiter, = plt.plot([], [], 'ko', ms = 4, mfc = 'yellow')

def animate(i):
    terre.set_data(x_terre[i], y_terre[i])
    jupiter.set_data(x_jupiter[i], y_jupiter[i])
    return terre, jupiter,



anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 20, blit = True, repeat = True)



plt.show()