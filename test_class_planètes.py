import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planètes import *  #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv


x_min, x_max = 0, 10000
y_min, y_max = 0, 10000


fig, ax = plt.subplots(1, 1) #définiton de notre figure composé de seulement une ligne et une colonne
ax = plt.gca() #prendre en compte les axes actuels

ax.set_facecolor((1, 1, 1))  #fond de notre plot en noir


plt.xlim([x_min, x_max]) #definie la scale de notre plot
plt.ylim([y_min, y_max])



class Planète:
    def __init__(self, color, nb_frame, size, coord_x, coord_y):
        self.color = color
        self.nb_frame = nb_frame
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
    


    
Mercure = Planète('red', frame_Mercure, 2.439, x_Mercure, y_Mercure)
Venus = Planète('red', frame_Venus, 6.052, x_Venus, y_Venus)
Terre = Planète('red', frame_Terre, 6.378, x_Terre, y_Terre)
Mars = Planète('red', frame_Mars, 3.397, x_Mars, y_Mars)
Jupiter = Planète('red', frame_Jupiter, 17.500, x_Jupiter, y_Jupiter)
Saturne = Planète('red', frame_Saturne, 16.300, x_Saturne, y_Saturne)
Uranus = Planète('red', frame_Uranus, 15.6, x_Urnaus, y_Uranus)
Neptune = Planète('red', frame_Neptune, 14.8, x_Neptune, y_Neptune)




Mercure_plt, = plt.plot([], [], 'ko', ms = Mercure.size, mfc = Mercure.color)
Venus_plt, = plt.plot([], [], 'ko', ms = Venus.size, mfc = Venus.color)
Terre_plt, = plt.plot([], [], 'ko', ms = Terre.size, mfc = Terre.color)
Mars_plt, = plt.plot([], [], 'ko', ms = Mars.size, mfc = Mars.color)
Jupiter_plt, = plt.plot([], [], 'ko', ms = Jupiter.size, mfc = Jupiter.color)
Saturne_plt, = plt.plot([], [], 'ko', ms = Saturne.size, mfc = Saturne.color)
Uranus_plt, = plt.plot([], [], 'ko', ms = Uranus.size, mfc = Uranus.color)
Neptune_plt, = plt.plot([], [], 'ko', ms = Neptune.size, mfc = Neptune.color)


#Asteroide, = plt.plot([], [], 'ko', ms = 3, mfc = 'blue')


def animate_Mercure(i):
    Mercure_plt.set_data(Mercure.coord_x[i], Mercure.coord_y[i])
    return Mercure_plt  
    
def animate_Venus(i):
    Venus_plt.set_data(Venus.coord_x[i], Venus.coord_y[i])
    return Venus_plt

def animate_Terre(i):
    Terre_plt.set_data(Terre.coord_x[i], Terre.coord_y[i])
    return Terre_plt

def animate_Mars(i):
    Mars_plt.set_data(Mars.coord_x[i], Mars.coord_y[i])
    return Mars_plt

def animate_Jupiter(i):
    Jupiter_plt.set_data(Jupiter.coord_x[i], Jupiter.coord_y[i])
    return Jupiter_plt

def animate_Saturne(i):
    Saturne_plt.set_data(Saturne.coord_x[i], Saturne.coord_y[i])
    return Saturne_plt

def animate_Uranus(i):
    Uranus_plt.set_data(Uranus.coord_x[i], Uranus.coord_y[i])
    return Uranus_plt


def animate_Neptune(i):
    Neptune_plt.set_data(Neptune.coord_x[i], Neptune.coord_y[i])
    return Neptune_plt



anim_Mercure = animation.FuncAnimation(fig, animate_Mercure, frames = Mercure.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Venus = animation.FuncAnimation(fig, animate_Venus, frames = Venus.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Terre = animation.FuncAnimation(fig, animate_Terre, frames = Terre.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Mars = animation.FuncAnimation(fig, animate_Mars, frames = Mars.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Jupiter = animation.FuncAnimation(fig, animate_Jupiter, frames = Jupiter.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Saturne = animation.FuncAnimation(fig, animate_Saturne, frames = Saturne.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Uranus = animation.FuncAnimation(fig, animate_Uranus, frames = Uranus.nb_frame ,interval = 1, blit = False, repeat = True)

anime_Neptune = animation.FuncAnimation(fig, animate_Neptune, frames = Neptune.nb_frame ,interval = 1, blit = False, repeat = True)


plt.grid(alpha = 0.2)
plt.show()

