import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planètes import *  #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv


x_min, x_max = 0, 10000
y_min, y_max = 0, 10000


fig, ax = plt.subplots(1, 1) #définiton de notre figure composé de seulement une ligne et une colonne
ax = plt.gca() #prendre en compte les axes actuels

ax.set_facecolor((0, 0, 0))  #fond de notre plot en noir


plt.xlim([x_min, x_max]) #definie la scale de notre plot
plt.ylim([y_min, y_max])


"""
class Planète:
    def __init__(self, color, nb_frame, size, coord_x, coord_y):
        self.color = color
        self.nb_frame = nb_frame
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
"""       




Mercure, = plt.plot([], [], 'ko', ms = 2.439, mfc = 'red')
Venus, = plt.plot([], [], 'ko', ms = 6.052, mfc = 'red')
Terre, = plt.plot([], [], 'ko', ms = 6.378, mfc = 'red')
Mars, = plt.plot([], [], 'ko', ms = 3.397, mfc = 'red')
Jupiter, = plt.plot([], [], 'ko', ms = 17.500, mfc = 'yellow')
Saturne, = plt.plot([], [], 'ko', ms = 16.300, mfc = 'red')
Uranus, = plt.plot([], [], 'ko', ms = 15.600, mfc = 'red')
Neptune, = plt.plot([], [], 'ko', ms = 14.800, mfc = 'red')
Asteroide, = plt.plot([], [], 'ko', ms = 3, mfc = 'blue')

"""
list_frame = [frame_Asteroide]

for elem in nom_planètes:
    frame = 'frame_' + elem
    list_frame.append(frame)

print(list_frame)
"""


list_frame = [frame_Mercure, frame_Venus, frame_Terre, frame_Mars, frame_Jupiter, frame_Saturne, frame_Uranus, frame_Neptune, frame_Asteroide]
print(list_frame)





def animate(i):

    Mercure.set_data(x_Mercure[i], y_Mercure[i])
    Venus.set_data(x_Venus[i], y_Venus[i])
    Terre.set_data(x_Terre[i], y_Terre[i])
    Mars.set_data(x_Mars[i], y_Mars[i])
    Jupiter.set_data(x_Jupiter[i], y_Jupiter[i])
    Saturne.set_data(x_Saturne[i], y_Saturne[i])
    Uranus.set_data(x_Urnaus[i], y_Uranus[i])
    Neptune.set_data(x_Neptune[i], y_Neptune[i])
    Asteroide.set_data(x_Asteroide[i], y_Asteroide[i])
    print(i, x_Asteroide[i])

    return Mercure, Venus, Terre, Mars, Jupiter, Saturne, Uranus, Neptune, Asteroide



anim = animation.FuncAnimation(fig, animate, frames= 2019 ,interval = 1, blit = False, repeat = True)


plt.grid(alpha = 0.2)
plt.show()

