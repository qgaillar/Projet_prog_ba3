import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.core.fromnumeric import size
from planètes import *  #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv
from asteroide_coor import *
from matplotlib.widgets import Slider, Button


#---initialisation variables----#

x_min, x_max = 0, 10e6
y_min, y_max = 0, 10e6
G = 6.67*10e-11                #[m^3/(kg^-1*s^-2)]
#x_Asteroid_init = 400000
#y_Asteroid_init = 5*10e5

#theta_0 = 0
#theta_1 = np.pi/4
#theta_2 = np.pi/2
#theta_3 = 5*np.pi/6


#theta = theta_3 # degrès 

#---initialisation de notre figure----#

fig = plt.figure()
ax = plt.subplot(111) #définiton de notre figure composé de seulement une ligne et une colonne
#ax = plt.gca() #prendre en compte les axes actuels
ax.set_facecolor((0, 0, 0))  #fond de notre plot en noir
#plt.subplots_adjust(bottom=0.2)


plt.xlim([x_min, x_max]) #definie la scale de notre plot
plt.ylim([y_min, y_max])



#----définition des classes----#


class Planète:
    def __init__(self, name, color, nb_frame, size, coord_x, coord_y, mass, cos_planete, sin_planete, rayon_collision):
        self.name = name
        self.color = color
        self.nb_frame = nb_frame
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass
        self.cos_planete = cos_planete
        self.sin_planete = sin_planete
        self.rayon_collision = rayon_collision

class Asteroid:
    def __init__(self, color, size, mass, coord_x_init, coord_y_init, coord_x, coord_y, vitesse):
        self.color = color
        self.size = size
        self.mass = mass
        self.coord_x_init = coord_x_init
        self.coord_y_init = coord_y_init
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.vitesse = vitesse

class Etoile:
    def __init__(self, name, color, size, mass, coord_x, coord_y, cos_etoile, sin_etoile, rayon_collision):
        self.name = name
        self.color = color
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass
        self.cos_etoile = cos_etoile
        self.sin_etoile = sin_etoile
        self.rayon_collision = rayon_collision

#----def coord asteroid init----#

x = valeur_coor ()   
y = valeur_coor ()

asteroide_x_init = int(x)
asteroide_y_init = int(y)

while (asteroide_x_init >1000000 and asteroide_x_init < 9000000) and (asteroide_y_init > 1000000 and asteroide_y_init < 9000000 != True):
    print("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 100000 ou 900000 et 1000000")
    y = valeur_coor()
    asteroide_y_init = int(y)
        
theta = int(input('saisissez un angle de depart: '))

V0 = float(input("vitesse initiale de l'asteroide [10^3km/j]"))


#---- definitions des astres-----#


Mercure = Planète('Mercure', 'blue', frame_Mercure, 6, x_Mercure, y_Mercure, 33e22, 0, 0, Rayon_collision_planete[0]) #0.2439*5
Venus = Planète('Venus','red', frame_Venus, 0.6052*5, x_Venus, y_Venus, 490e22, 0, 0, Rayon_collision_planete[1])
Terre = Planète('Terre','red', frame_Terre, 0.6378*5, x_Terre, y_Terre, 600e22, 0, 0, Rayon_collision_planete[2])
Mars = Planète('Mars','red', frame_Mars, 0.3397*5, x_Mars, y_Mars, 64e22, 0, 0, Rayon_collision_planete[3])
Jupiter = Planète('Jupiter','red', frame_Jupiter, 7.1500, x_Jupiter, y_Jupiter, 190000e22, 0, 0,Rayon_collision_planete[4])
Saturne = Planète('Saturne', 'lime', frame_Saturne, 6.0300, x_Saturne, y_Saturne, 5700e22, 0, 0, Rayon_collision_planete[5])
Uranus = Planète('Uranus', 'blue', frame_Uranus, 10, x_Urnaus, y_Uranus, 8700e22, 0, 0, Rayon_collision_planete[6]) #2.56
Neptune = Planète('Neptune','green', frame_Neptune, 6, x_Neptune, y_Neptune, 10000e22, 0, 0,Rayon_collision_planete[7]) #2.48
Soleil = Etoile('Soleil','lime', 10, x_max/2, y_max/2,  1.989e30, 0, 0, Rayon_collision_planete[8]) # x_max/2 - 1.5*10e5
Asteroid_crash_test = Asteroid('red', 5,  10e18, asteroide_x_init, asteroide_y_init, 0, 0, V0)

list_planete = [Mercure, Venus, Terre, Mars, Jupiter, Saturne, Uranus, Neptune]


#---definition des plots des astres----#

"""
Mercure_plt, = plt.plot([], [], 'ko', ms = Mercure.size, mfc = Mercure.color, label = 'Mercure')  #ko = pour former un cercle avec contour noir
Venus_plt, = plt.plot([], [], 'ko', ms = Venus.size, mfc = Venus.color, label = 'Venus')
Terre_plt, = plt.plot([], [], 'ko', ms = Terre.size, mfc = Terre.color)
Mars_plt, = plt.plot([], [], 'ko', ms = Mars.size, mfc = Mars.color)
Jupiter_plt, = plt.plot([], [], 'ko', ms = Jupiter.size, mfc = Jupiter.color)
Saturne_plt, = plt.plot([], [], 'ko', ms = Saturne.size, mfc = Saturne.color)
Uranus_plt, = plt.plot([], [], 'ko', ms = Uranus.size, mfc = Uranus.color)
Neptune_plt, = plt.plot([], [], 'ko', ms = Neptune.size, mfc = Neptune.color)
Asteroid_crash_test_plt, = plt.plot([asteroide_x_init], [asteroide_y_init], 'ko', ms = Asteroid_crash_test.size, mfc = Asteroid_crash_test.color)
Asteroid_line, = plt.plot([],[], color = Asteroid_crash_test.color, ls = '--', ms = 1, alpha = 0.4, label = 'Asteroid line')
Soleil_plt, = plt.plot([Soleil.coord_x], [Soleil.coord_y], 'yo', ms = Soleil.size, mfc = Soleil.color)
"""
Mercure_plt, = plt.plot([], [], 'ko', ms = Mercure.size, mfc = Mercure.color, label = 'Mercure')  #ko = pour former un cercle avec contour noir
Venus_plt, = plt.plot([], [], 'ko', ms = Venus.size, mfc = Venus.color, label = 'Venus')
Terre_plt, = plt.plot([], [], 'ko', ms = Terre.size, mfc = Terre.color, label = 'Terre')
Mars_plt, = plt.plot([], [], 'ko', ms = Mars.size, mfc = Mars.color, label = 'Mars')
Jupiter_plt, = plt.plot([], [], 'ko', ms = Jupiter.size, mfc = Jupiter.color, label = 'Jupiter')
Saturne_plt, = plt.plot([], [], 'ko', ms = Saturne.size, mfc = Saturne.color, label = 'Saturne')
Uranus_plt, = plt.plot([], [], 'ko', ms = Uranus.size, mfc = Uranus.color, label = 'Uranus')
Neptune_plt, = plt.plot([], [], 'ko', ms = Neptune.size, mfc = Neptune.color, label = 'Neptune')
Asteroid_crash_test_plt, = plt.plot([], [], 'ko', ms = Asteroid_crash_test.size, mfc = Asteroid_crash_test.color, label = 'Asteroid')
Asteroid_line, = plt.plot([],[], color = Asteroid_crash_test.color, ls = '--', ms = 1, alpha = 0.4, label = 'Asteroid line')
Soleil_plt, = plt.plot([Soleil.coord_x], [Soleil.coord_y], 'ko', ms = Soleil.size, mfc = Soleil.color, label = 'Soleil')

list_plot_planete = [Mercure_plt, Venus_plt, Terre_plt, Mars_plt, Jupiter_plt, Saturne_plt, Uranus_plt, Neptune_plt]

"""
# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)
"""


#----calculs attraction gravitationnelle-----#


def Fg(mass_planète, x_Asteroid_crash_test, y_Asteroid_crash_test, x_planète, y_planète):
    delta_x = x_Asteroid_crash_test - x_planète
    delta_y = y_Asteroid_crash_test - y_planète
    dist = np.sqrt(delta_x**2 + delta_y**2)
    Force_gravitationnelle = (G * mass_planète * Asteroid_crash_test.mass) / (dist * 10e3)**2  #10e3 = conversion en mètres
    #print(Force_gravitationnelle)
    return Force_gravitationnelle


def Fg_totale_x(x_Asteroid_crash_test, y_Asteroid_crash_test, i):


    Fg_tot_x = 0
    """
    cos_Mercure = (abs(x_Asteroid_crash_test - Mercure.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mercure.coord_x[i])**2 + (y_Asteroid_crash_test - Mercure.coord_y[i])**2))
    cos_Venus = (abs(x_Asteroid_crash_test - Venus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2))
    cos_Terre = (abs(x_Asteroid_crash_test - Terre.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2))
    cos_Mars = (abs(x_Asteroid_crash_test - Mars.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2))
    cos_Jupiter = (abs(x_Asteroid_crash_test - Jupiter.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2))
    cos_Saturne = (abs(x_Asteroid_crash_test - Saturne.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2))
    cos_Uranus = (abs(x_Asteroid_crash_test - Uranus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2))
    cos_Neptune = (abs(x_Asteroid_crash_test - Neptune.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2))
    cos_Soleil = (abs(x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))
    """
    #"""
    for j in range(0,len(list_planete)):
        list_planete[j].cos_planete = (abs(x_Asteroid_crash_test - list_planete[j].coord_x[i]) / np.sqrt((x_Asteroid_crash_test - list_planete[j].coord_x[i])**2 + (y_Asteroid_crash_test - list_planete[j].coord_y[i])**2))
        Fg_tot_x += Fg(list_planete[j].mass, x_Asteroid_crash_test, y_Asteroid_crash_test, list_planete[j].coord_x[i], list_planete[j].coord_y[i]) * list_planete[j].cos_planete
    Soleil.cos_etoile = (abs(x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2)) 
    Fg_tot_x += Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * Soleil.cos_etoile
    """
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
    """
    return Fg_tot_x

def Fg_totale_y(x_Asteroid_crash_test, y_Asteroid_crash_test, i):
    #"""
    Fg_tot_y = 0
    for j in range(0,len(list_planete)):
        list_planete[j].sin_planete = (abs(y_Asteroid_crash_test - list_planete[j].coord_y[i]) / np.sqrt((x_Asteroid_crash_test - list_planete[j].coord_x[i])**2 + (y_Asteroid_crash_test - list_planete[j].coord_y[i])**2))
        Fg_tot_y += Fg(list_planete[j].mass, x_Asteroid_crash_test, y_Asteroid_crash_test, list_planete[j].coord_x[i], list_planete[j].coord_y[i]) * list_planete[j].sin_planete
    Soleil.sin_etoile = (abs(y_Asteroid_crash_test - Soleil.coord_y) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_y)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))
    Fg_tot_y += Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * Soleil.sin_etoile
    #"""
    """
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
    """
    return Fg_tot_y


#-------Calculs des coordonées de notre Asteroide-----#

coord_x_Asteroid = [asteroide_x_init]
coord_y_Asteroid = [asteroide_y_init]

def coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, j, V0, theta):

    for i in range(0, j):

        condition_vitesse_initiale_x = Asteroid_crash_test.vitesse * (i+1) * np.cos(theta)
        condition_vitesse_initiale_y = Asteroid_crash_test.vitesse * (i+1) * np.sin(theta)

        x_Asteroid_crash_test = coord_x_Asteroid[i] + ((Fg_totale_x(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + condition_vitesse_initiale_x
        y_Asteroid_crash_test = coord_y_Asteroid[i] + ((Fg_totale_y(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + condition_vitesse_initiale_y

        coord_x_Asteroid.append(x_Asteroid_crash_test)
        coord_y_Asteroid.append(y_Asteroid_crash_test)

    return np.array(coord_x_Asteroid), np.array(coord_y_Asteroid)


coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, 60000, V0, theta)

Asteroid_crash_test.coord_x = coord_x_Asteroid 
Asteroid_crash_test.coord_y = coord_y_Asteroid

print("Aquisition des coordonnées de notre Asteroid = ok !")

def distance_asteroid_planete(x_asteroid, y_asteroid, x_planete, y_planete):
    distance_A_P = np.sqrt((x_asteroid - x_planete)**2 + (y_asteroid - y_planete)**2)
    return distance_A_P

def collision(distance, rayon, name):
    if distance <= 500000: #normalement ici on met le rayon de collision de chaque planète
        print("collision avec", name)
        plt.text(4000000, 8000000, 'Collision avec ' + name, color = 'red', fontsize = 15)

def exit_solar_syst(coord_x, coord_y, animation_launching):
    marge = 100000
    if coord_x < x_min - marge or coord_x > x_max + marge or coord_y < y_min - marge or coord_y > y_max + marge:
        plt.text(2000000, 8000000, "Asteroid is out of solar system", color = 'red', fontsize = 15)
        #animation_launching = False
        

#coord_x_Asteroid, coord_y_Asteroid = coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, 60000, V0, theta)

#----fonctions de mise en mouvement des astres-----#
"""
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
"""

interval_time = 1.0

def run_animation():
    anim_running = True

    def onClick(event):
        nonlocal anim_running
        if anim_running:
            anim.event_source.stop()
            anim_running = False
        else:
            anim.event_source.start()
            anim_running = True
    def anim_astre(i):
        nonlocal anim_running
        Asteroid_crash_test_plt.set_data(Asteroid_crash_test.coord_x[i], Asteroid_crash_test.coord_y[i])
        Asteroid_line.set_data(Asteroid_crash_test.coord_x[:i], Asteroid_crash_test.coord_y[:i])

        for j in range(len(list_plot_planete)):
            list_plot_planete[j].set_data(list_planete[j].coord_x[i], list_planete[j].coord_y[i])
            distance_A_P = distance_asteroid_planete(Asteroid_crash_test.coord_x[i], Asteroid_crash_test.coord_y[i], list_planete[j].coord_x[i], list_planete[j].coord_y[i])
            #print(distance_A_P)
        return Asteroid_crash_test_plt, Asteroid_line, list_planete                
    

    fig.canvas.mpl_connect('button_press_event', onClick)
    anim = animation.FuncAnimation(fig, anim_astre, frames = Neptune.nb_frame ,interval = interval_time, blit = False, repeat = True)
    #if collision == True:
        #anim.event_source.stop()       


#print("lancment de l'Asteroid aux coordonnées: ", Asteroid_crash_test.coord_x_init,",", Asteroid_crash_test.coord_y_init, "avec un angle de ", theta, "et une vitesse initiale de ", V0)

"""
class Index(object):

    def lunch_animation(self, event):
        run_animation()

callback = Index()
axnext = plt.axes([0.1, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Animate')
bnext.on_clicked(callback.lunch_animation)
"""


#plt.subplots_adjust(left = 0.25, bottom = 0.25)
#lunch_animation = plt.axes([0.8, 0.025, 0.1, 0.04])
#button = Button(lunch_animation, 'Animate', hovercolor='0.975')

#run_animation()
#animation_astreroid = run_animation()

run_animation()

"""
for a in range(0, 60000):
    for b in range(0, len(list_planete)):
        distance_A_P = distance_asteroid_planete(Asteroid_crash_test.coord_x[a], Asteroid_crash_test.coord_y[a], list_planete[b].coord_x[a], list_planete[b].coord_y[a])
        collision(distance_A_P, list_planete[b].rayon_collision, list_planete[b].name) 
        exit_solar_syst(Asteroid_crash_test.coord_x[a], Asteroid_crash_test.coord_y[a], animation_astreroid)

"""



#il faut creer le CSV des rayon de collision et les attribuer à chaque planéte
if asteroide_x_init < 5000000:
    plt.text(5000000, 600000, "coordonnée initiale x de notre l'Asteroid: " + str(Asteroid_crash_test.coord_x_init), color = 'red', fontsize = 7)
    plt.text(5000000, 200000, "coordonnée initiale y de notre l'Asteroid: " + str(Asteroid_crash_test.coord_y_init), color = 'red', fontsize = 7)
else:
    plt.text(100000, 600000, "coordonnée initiale x de notre l'Asteroid: " + str(Asteroid_crash_test.coord_x_init), color = 'red', fontsize = 7)
    plt.text(100000, 200000, "coordonnée initiale y de notre l'Asteroid: " + str(Asteroid_crash_test.coord_y_init), color = 'red', fontsize = 7)


"""
axangle = plt.axes([0.25, 0.1, 0.65, 0.03])
angle_slider = Slider(
    ax=axangle,
    label='angle (°)',
    valmin=0,
    valmax=360,
    valinit = theta,
)

def update(val):
    theta.set_ydata(angle_slider)
    fig.canvas.draw_idle()


angle_slider.on_changed(update) 
"""

plt.title("Asteroid trajectory simulation")
plt.grid(alpha = 0.2)
plt.legend()
plt.show()

plt.show()
