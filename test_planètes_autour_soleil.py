import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planètes import *  #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv


x_min, x_max = 0, 10000
y_min, y_max = 0, 10000


fig, ax = plt.subplots(1, 1) #définiton de notre figure composé de seulement une ligne et une colonne
ax = plt.gca() #prendre en compte les axes actuels

ax.set_facecolor((0, 0, 0))  #fond de notre plot en noir


plt.xlim([x_min, x_max])
plt.ylim([y_min, y_max])


Mercure, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Venus, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Terre, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Mars, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Jupiter, = plt.plot([], [], 'ko', ms = 4, mfc = 'yellow')
Saturne, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Uranus, = plt.plot([], [], 'ko', ms = 3, mfc = 'red')
Neptune, = plt.plot([], [], 'ko', ms = 5, mfc = 'red')

def animate(i):

    Mercure.set_data(x_Mercure[i], y_Mercure[i])
    Venus.set_data(x_Venus[i], y_Venus[i])
    Terre.set_data(x_Terre[i], y_Terre[i])
    Mars.set_data(x_Mars[i], y_Mars[i])
    Jupiter.set_data(x_Jupiter[i], y_Jupiter[i])
    Saturne.set_data(x_Saturne[i], y_Saturne[i])
    Uranus.set_data(x_Urnaus[i], y_Uranus[i])
    Neptune.set_data(x_Neptune, y_Neptune)
    print(i, x_Neptune[i])




    return Mercure, Venus, Terre, Mars, Jupiter, Saturne, Uranus, Neptune



anim = animation.FuncAnimation(fig, animate, frames = 400, interval = 100, blit = True, repeat = True)



plt.show()