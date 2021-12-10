import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.core.fromnumeric import size
from planètes import *  #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv
from asteroide_coor import *



#---initialisation variables----#

x_min, x_max = 0, 10e6
y_min, y_max = 0, 10e6
G = 6.7e-11                #[m^3/(kg^-1*s^-2)]
#x_Asteroid_init = 400000
#y_Asteroid_init = 5*10e5
V0 = 2 # m.s
theta = 0 # degrès 

#---initialisation de notre figure----#

fig, ax = plt.subplots(1, 1) #définiton de notre figure composé de seulement une ligne et une colonne
ax = plt.gca() #prendre en compte les axes actuels

ax.set_facecolor((0, 0, 0))  #fond de notre plot en noir


plt.xlim([x_min, x_max]) #definie la scale de notre plot
plt.ylim([y_min, y_max])


#----définition des classes----#


class Planète:
    def __init__(self, color, nb_frame, size, coord_x, coord_y, mass):
        self.color = color
        self.nb_frame = nb_frame
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass

class Asteroid:
    def __init__(self, color, size, mass):
        self.color = color
        self.size = size
        self.mass = mass
        #self.coord_x_init = coord_x_init
        #self.coord_y_init = coord_y_init

class Etoile:
    def __init__(self, color, size, mass, coord_x, coord_y):
        self.color = color
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass

#----def coord asteroid init----#

x = valeur_coor ()   
y = valeur_coor ()

asteroide_x_init = int(x)
asteroide_y_init = int(y)

while (asteroide_x_init >1000000 and asteroide_x_init < 9000000) and (asteroide_y_init > 1000000 and asteroide_y_init < 9000000 != True):
    print("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 100000 ou 900000 et 1000000")
    y = valeur_coor()
    asteroide_y_init = int(y)
print("Modelisation in process...")
        

#---- definitions des astres-----#


Mercure = Planète('red', frame_Mercure, 0.2439*5, x_Mercure, y_Mercure, 33e22)
Venus = Planète('red', frame_Venus, 0.6052*5, x_Venus, y_Venus, 490e22)
Terre = Planète('red', frame_Terre, 0.6378*5, x_Terre, y_Terre, 600e22)
Mars = Planète('red', frame_Mars, 0.3397*5, x_Mars, y_Mars, 64e22)
Jupiter = Planète('red', frame_Jupiter, 7.1500, x_Jupiter, y_Jupiter, 190000e22)
Saturne = Planète('red', frame_Saturne, 6.0300, x_Saturne, y_Saturne, 5700e22)
Uranus = Planète('red', frame_Uranus, 2.56, x_Urnaus, y_Uranus, 8700e22)
Neptune = Planète('red', frame_Neptune, 6, x_Neptune, y_Neptune, 10000e22) #2.48
Soleil = Etoile('yellow', 3, 4.9985 * 10e5, 5 * 10e5,  1.989e30)
Asteroid_crash_test = Asteroid('red', size= 5, mass= 10e18)



#---definition des plots des astres----#

Mercure_plt, = plt.plot([], [], 'ko', ms = Mercure.size, mfc = Mercure.color)  #ko = pour former un cercle avec contour noir
Venus_plt, = plt.plot([], [], 'ko', ms = Venus.size, mfc = Venus.color)
Terre_plt, = plt.plot([], [], 'ko', ms = Terre.size, mfc = Terre.color)
Mars_plt, = plt.plot([], [], 'ko', ms = Mars.size, mfc = Mars.color)
Jupiter_plt, = plt.plot([], [], 'ko', ms = Jupiter.size, mfc = Jupiter.color)
Saturne_plt, = plt.plot([], [], 'ko', ms = Saturne.size, mfc = Saturne.color)
Uranus_plt, = plt.plot([], [], 'ko', ms = Uranus.size, mfc = Uranus.color)
Neptune_plt, = plt.plot([], [], 'ko', ms = Neptune.size, mfc = Neptune.color)
Asteroid_crash_test_plt, = plt.plot([asteroide_x_init], [asteroide_y_init], 'ko', ms = Asteroid_crash_test.size, mfc = Asteroid_crash_test.color)
Soleil_plt, = plt.plot([Soleil.coord_x], [Soleil.coord_y], 'yo', ms = Soleil.size, mfc = Soleil.color)




#----calculs attraction gravitationnelle-----#


def Fg(mass_planète, x_Asteroid_crash_test, y_Asteroid_crash_test, x_planète, y_planète):
    delta_x = x_Asteroid_crash_test - x_planète
    delta_y = y_Asteroid_crash_test - y_planète
    dist = np.sqrt(delta_x**2 + delta_y**2)
    Force_gravitationnelle = (G * mass_planète * Asteroid_crash_test.mass) / (dist * 10e3)**2  #10e3 = conversion en mètres
    return Force_gravitationnelle


def Fg_totale_x(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    cos_Mercure = (abs(x_Asteroid_crash_test - Mercure.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mercure.coord_x[i])**2 + (y_Asteroid_crash_test - Mercure.coord_y[i])**2))
    cos_Venus = (abs(x_Asteroid_crash_test - Venus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2))
    cos_Terre = (abs(x_Asteroid_crash_test - Terre.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2))
    cos_Mars = (abs(x_Asteroid_crash_test - Mars.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2))
    cos_Jupiter = (abs(x_Asteroid_crash_test - Jupiter.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2))
    cos_Saturne = (abs(x_Asteroid_crash_test - Saturne.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2))
    cos_Uranus = (abs(x_Asteroid_crash_test - Uranus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2))
    cos_Neptune = (abs(x_Asteroid_crash_test - Neptune.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2))
    cos_Soleil = (abs(x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))

    Fg_tot_x = (
        Fg(Mercure.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mercure.coord_x[i], Mercure.coord_y[i]) * cos_Mercure + #pb avec Fg qui génère 1705 valeurs d'un coup 
        Fg(Venus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Venus.coord_x[i], Venus.coord_y[i]) * cos_Venus +
        Fg(Terre.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Terre.coord_x[i], Terre.coord_y[i]) * cos_Terre +
        Fg(Mars.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mars.coord_x[i], Mars.coord_y[i]) * cos_Mars +
        Fg(Jupiter.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Jupiter.coord_x[i], Jupiter.coord_y[i]) * cos_Jupiter +
        Fg(Saturne.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Saturne.coord_x[i], Saturne.coord_y[i]) * cos_Saturne +
        Fg(Uranus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Uranus.coord_x[i], Uranus.coord_y[i]) * cos_Uranus +
        Fg(Neptune.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Neptune.coord_x[i], Neptune.coord_y[i]) * cos_Neptune +
        Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * cos_Soleil
    )
    return Fg_tot_x

def Fg_totale_y(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    sin_Mercure = (abs(y_Asteroid_crash_test - Mercure.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Mercure.coord_x[i])**2 + (y_Asteroid_crash_test - Mercure.coord_y[i])**2))
    sin_Venus = (abs(y_Asteroid_crash_test - Venus.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2))
    sin_Terre = (abs(y_Asteroid_crash_test - Terre.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2))
    sin_Mars = (abs(y_Asteroid_crash_test - Mars.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2))
    sin_Jupiter = (abs(y_Asteroid_crash_test - Jupiter.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2))
    sin_Saturne = (abs(y_Asteroid_crash_test - Saturne.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2))
    sin_Uranus = (abs(y_Asteroid_crash_test - Uranus.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2))
    sin_Neptune = (abs(y_Asteroid_crash_test - Neptune.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2))
    sin_Soleil = (abs(y_Asteroid_crash_test - Soleil.coord_y) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_y)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))


    Fg_tot_y = (
        Fg(Mercure.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mercure.coord_x[i], Mercure.coord_y[i]) * sin_Mercure +
        Fg(Venus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Venus.coord_x[i], Venus.coord_y[i]) * sin_Venus +
        Fg(Terre.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Terre.coord_x[i], Terre.coord_y[i]) * sin_Terre +
        Fg(Mars.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mars.coord_x[i], Mars.coord_y[i]) * sin_Mars +
        Fg(Jupiter.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Jupiter.coord_x[i], Jupiter.coord_y[i]) * sin_Jupiter +
        Fg(Saturne.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Saturne.coord_x[i], Saturne.coord_y[i]) * sin_Saturne +
        Fg(Uranus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Uranus.coord_x[i], Uranus.coord_y[i]) * sin_Uranus +
        Fg(Neptune.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Neptune.coord_x[i], Neptune.coord_y[i]) * sin_Neptune +
        Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * sin_Soleil
    )
    return Fg_tot_y

coord_x_Asteroid = [asteroide_x_init]
coord_y_Asteroid = [asteroide_y_init]

def coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, j, V0, theta):

    for i in range(0, j):

        x_Asteroid_crash_test = coord_x_Asteroid[i] + ((Fg_totale_x(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + V0 * (i+1) * np.cos(theta)
        y_Asteroid_crash_test = coord_y_Asteroid[i] + ((Fg_totale_y(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + V0 * (i+1) * np.sin(theta)

        coord_x_Asteroid.append(x_Asteroid_crash_test)
        coord_y_Asteroid.append(y_Asteroid_crash_test)

    return np.array(coord_x_Asteroid), np.array(coord_y_Asteroid)


coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, 60000, V0, theta)

def distance_asteroid_planete(x_asteroid, y_asteroid, x_planete, y_planete):
    distance_A_P = np.sqrt((x_asteroid - x_planete)**2 + (y_asteroid - y_planete)**2)
    return distance_A_P

def collision(distance, rayon):
    if distance <= rayon:
        plt.text(600000, 8000000, 'COLLISION !', color = 'red', weigth = 'bold', fontsize = 15)



#coord_x_Asteroid, coord_y_Asteroid = coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, 60000, V0, theta)

#----fonctions de mise en mouvement des astres-----#

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

def animate_Asteroid(i):
    Asteroid_crash_test_plt.set_data(coord_x_Asteroid[i], coord_y_Asteroid[i])
    return Asteroid_crash_test_plt


#---mise en mouvement des astres----#


interval_time = 1 #interval = ms between frames

anim_Mercure = animation.FuncAnimation(fig, animate_Mercure, frames = Mercure.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Venus = animation.FuncAnimation(fig, animate_Venus, frames = Venus.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Terre = animation.FuncAnimation(fig, animate_Terre, frames = Terre.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Mars = animation.FuncAnimation(fig, animate_Mars, frames = Mars.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Jupiter = animation.FuncAnimation(fig, animate_Jupiter, frames = Jupiter.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Saturne = animation.FuncAnimation(fig, animate_Saturne, frames = Saturne.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Uranus = animation.FuncAnimation(fig, animate_Uranus, frames = Uranus.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Neptune = animation.FuncAnimation(fig, animate_Neptune, frames = Neptune.nb_frame ,interval = interval_time, blit = False, repeat = True)

anim_Asteroid = animation.FuncAnimation(fig, animate_Asteroid, frames = len(coord_x_Asteroid) ,interval = interval_time, blit = False, repeat = True)





plt.grid(alpha = 0.2)
plt.show()

