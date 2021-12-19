
#----importation des modules----#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planètes import *                                 #fonction qui attribue à chaque planètes ses coord x et y grâce ouverture fichier csv

#---initialisation variables----#

x_min, x_max = 0, 10e6
y_min, y_max = 0, 10e6
G = 6.67*10e-11
interval_time = 1.0
boom = False
out = False                           

#---initialisation de notre figure----#

fig = plt.figure()
ax = plt.subplot(111)                                 #définiton de notre figure composé de seulement une ligne et une colonne
ax.set_facecolor((0, 0, 0))                           #fond de notre plot en noir


plt.xlim([x_min, x_max])                              #definie l'échelle de notre plot
plt.ylim([y_min, y_max])



#----définition des classes----#


class Planète:
    def __init__(self, name, color, nb_frame, size, coord_x, coord_y, mass, rayon_collision):
        self.name = name
        self.color = color
        self.nb_frame = nb_frame
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass
        #self.cos_planete = cos_planete
        #self.sin_planete = sin_planete
        self.rayon_collision = rayon_collision

class Asteroid:
    def __init__(self, color, size, mass, coord_x_init, coord_y_init, coord_x, coord_y, vitesse_x, vitesse_y, t):
        self.color = color
        self.size = size
        self.mass = mass
        self.coord_x_init = coord_x_init
        self.coord_y_init = coord_y_init
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
        self.t = t

class Etoile:
    def __init__(self, name, color, size, mass, coord_x, coord_y, rayon_collision):
        self.name = name
        self.color = color
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mass = mass
        #self.cos_etoile = cos_etoile
        #self.sin_etoile = sin_etoile
        self.rayon_collision = rayon_collision

#----def coord asteroid init----#


asteroide_x_init = x_Asteroid_init
asteroide_y_init = y_Asteroid_init       
asteroide_v_x_init = vitesse_x_Asteroid
asteroide_v_y_init = vitesse_y_Asteroid
t = nb_jour_lancement_init


#---- definitions des astres-----#


Mercure = Planète('Mercure', 'coral', frame_Mercure, 1, x_Mercure, y_Mercure, 33e22, Rayon_collision_planete[0]) #0.2439*5
Venus = Planète('Venus','darkorange', frame_Venus, 2.48, x_Venus, y_Venus, 490e22, Rayon_collision_planete[1])
Mars = Planète('Mars','orangered', frame_Mars, 2.615, x_Mars, y_Mars, 64e22, Rayon_collision_planete[2])
Terre = Planète('Terre','dodgerblue', frame_Terre, 1.393, x_Terre, y_Terre, 600e22, Rayon_collision_planete[3])
Jupiter = Planète('Jupiter','sandybrown', frame_Jupiter, 15.315, x_Jupiter, y_Jupiter, 190000e22,Rayon_collision_planete[4])
Saturne = Planète('Saturne', 'khaki', frame_Saturne, 10.723, x_Saturne, y_Saturne, 5700e22, Rayon_collision_planete[5])
Uranus = Planète('Uranus', 'deepskyblue', frame_Uranus, 5.496, x_Urnaus, y_Uranus, 8700e22, Rayon_collision_planete[6]) #2.56
Neptune = Planète('Neptune','royalblue', frame_Neptune, 5.168, x_Neptune, y_Neptune, 10000e22, Rayon_collision_planete[7]) #2.48
Soleil = Etoile('Soleil','yellow', 3, x_max/2, y_max/2,  1.989e30, Rayon_collision_planete[8]) # x_max/2 - 1.5*10e5
Asteroid_crash_test = Asteroid('red', 5,  10e15, asteroide_x_init, asteroide_y_init, 0, 0, asteroide_v_x_init, asteroide_v_y_init, t)
Asteroide_w_a = Asteroid('red', 5,  10e18, asteroide_x_init, asteroide_y_init, x_Asteroide_w_a, y_Asteroide_w_a, asteroide_v_x_init, asteroide_v_y_init, t)


list_planete = [Mercure, Venus, Terre, Mars, Jupiter, Saturne, Uranus, Neptune]


#---definition des plots des astres----#


Mercure_plt, = plt.plot([], [], 'ko', ms = Mercure.size, mfc = Mercure.color, label = 'Mercure')  #ko = pour former un cercle avec contour noir
Venus_plt, = plt.plot([], [], 'ko', ms = Venus.size, mfc = Venus.color, label = 'Venus')
Terre_plt, = plt.plot([], [], 'ko', ms = Terre.size, mfc = Terre.color, label = 'Terre')
Mars_plt, = plt.plot([], [], 'ko', ms = Mars.size, mfc = Mars.color, label = 'Mars')
Jupiter_plt, = plt.plot([], [], 'ko', ms = Jupiter.size, mfc = Jupiter.color, label = 'Jupiter')
Saturne_plt, = plt.plot([], [], 'ko', ms = Saturne.size, mfc = Saturne.color, label = 'Saturne')
Uranus_plt, = plt.plot([], [], 'ko', ms = Uranus.size, mfc = Uranus.color, label = 'Uranus')
Neptune_plt, = plt.plot([], [], 'ko', ms = Neptune.size, mfc = Neptune.color, label = 'Neptune')
Asteroid_crash_test_plt, = plt.plot([], [], 'ko', ms = Asteroid_crash_test.size, mfc = Asteroid_crash_test.color, label = 'Asteroid')
Asteroid_line, = plt.plot([],[], color = Asteroid_crash_test.color, ls = '--', ms = 1, alpha = 0.5, label = 'Asteroid line')
Soleil_plt, = plt.plot([x_max/2 - 1500], [y_max/2], 'ko', ms = Soleil.size, mfc = Soleil.color, label = 'Soleil')
Asteroid_w_a_line_plt, = plt.plot(x_Asteroide_w_a, y_Asteroide_w_a, color = "grey", ls = '--', ms = 1, alpha = 0.3, label = 'Asteroid line (without attraction)')


list_plot_planete = [Mercure_plt, Venus_plt, Terre_plt, Mars_plt, Jupiter_plt, Saturne_plt, Uranus_plt, Neptune_plt]


#----calculs attraction gravitationnelle-----#


def Fg(mass_planète, x_Asteroid_crash_test, y_Asteroid_crash_test, x_planète, y_planète):

    #cette fonction calcule la valeur de la force gravitationelle en 
    #fonction de comment l'asteroïde se situe par rapport a chacune des planètes

    Fg_finale_x = 0
    Fg_finale_y = 0
    delta_x = x_Asteroid_crash_test - x_planète
    delta_y = y_Asteroid_crash_test - y_planète
    dist = np.sqrt(delta_x**2 + delta_y**2)
    Force_gravitationnelle = (G * mass_planète * Asteroid_crash_test.mass) / (dist * 10e3)**2          #10e3 = conversion en mètres
    
    if y_planète == y_Asteroid_crash_test:
        if x_planète > x_Asteroid_crash_test:
            Fg_finale_x +=  Force_gravitationnelle
            return Fg_finale_x, Fg_finale_y
        else:
            Fg_finale_x -= Force_gravitationnelle 
            return Fg_finale_x, Fg_finale_y  
    
    elif x_planète == x_Asteroid_crash_test:
        if y_planète > y_Asteroid_crash_test:
            Fg_finale_y += Force_gravitationnelle
            return Fg_finale_x, Fg_finale_y
        else:
            Fg_finale_y -= Force_gravitationnelle
            return Fg_finale_x, Fg_finale_y

    elif x_planète > x_Asteroid_crash_test:
        if y_Asteroid_crash_test > y_planète:
            angle_planete = np.arctan((x_planète - x_Asteroid_crash_test) / (y_Asteroid_crash_test - y_planète))
            Fg_finale_x += Force_gravitationnelle * np.sin(angle_planete)
            Fg_finale_y -= Force_gravitationnelle * np.cos(angle_planete)
            return Fg_finale_x, Fg_finale_y
        else:
            angle_planete = np.arctan((y_planète - y_Asteroid_crash_test) / (x_planète - x_Asteroid_crash_test))
            Fg_finale_x += Force_gravitationnelle * np.cos(angle_planete)
            Fg_finale_y += Force_gravitationnelle * np.sin(angle_planete)
            return Fg_finale_x, Fg_finale_y

    elif x_planète < x_Asteroid_crash_test:
        if y_Asteroid_crash_test > y_planète:
            angle_planete = np.arctan((x_Asteroid_crash_test - x_planète) / (y_Asteroid_crash_test - y_planète))
            Fg_finale_x -= Force_gravitationnelle * np.sin(angle_planete)
            Fg_finale_y -= Force_gravitationnelle * np.cos(angle_planete)
            return Fg_finale_x, Fg_finale_y
        else:
            angle_planete = np.arctan((y_planète - y_Asteroid_crash_test) / (x_Asteroid_crash_test - x_planète))
            Fg_finale_x -= Force_gravitationnelle * np.cos(angle_planete)
            Fg_finale_y += Force_gravitationnelle * np.sin(angle_planete)
            return Fg_finale_x, Fg_finale_y


def Fg_totale_x(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    #cette fonction somme toutes les forces gravitationnelles selon l'axe x

    Fg_tot_x = 0
   
    for j in range(0,len(list_planete)):
        Fg_x, Fg_y = Fg(list_planete[j].mass, x_Asteroid_crash_test, y_Asteroid_crash_test, list_planete[j].coord_x[i], list_planete[j].coord_y[i])
        #adj = (x_Asteroid_crash_test - list_planete[j].coord_x[i])
        #hyp = np.sqrt((x_Asteroid_crash_test - list_planete[j].coord_x[i])**2 + (y_Asteroid_crash_test - list_planete[j].coord_y[i])**2)
        #list_planete[j].cos_planete = adj / hyp
        Fg_tot_x += Fg_x                                #* list_planete[j].cos_planete
    #Soleil.cos_etoile = (x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2)
    Fg_x_soleil, Fg_y_soleil = Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) 
    Fg_tot_x += Fg_x_soleil                             #* Soleil.cos_etoile
    return Fg_tot_x

def Fg_totale_y(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    #cette fonction somme toutes les forces gravitationnelles selon l'axe y
    
    Fg_tot_y = 0

    for j in range(0,len(list_planete)):
        Fg_x, Fg_y = Fg(list_planete[j].mass, x_Asteroid_crash_test, y_Asteroid_crash_test, list_planete[j].coord_x[i], list_planete[j].coord_y[i])
        #op = (y_Asteroid_crash_test - list_planete[j].coord_y[i])
        #hyp = np.sqrt((x_Asteroid_crash_test - list_planete[j].coord_x[i])**2 + (y_Asteroid_crash_test - list_planete[j].coord_y[i])**2)
        #list_planete[j].sin_planete = op / hyp 
        Fg_tot_y += Fg_y                            #* list_planete[j].sin_planete
    #Soleil.sin_etoile = (y_Asteroid_crash_test - Soleil.coord_y) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_y)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2)
    Fg_x_soleil, Fg_y_soleil = Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) 
    Fg_tot_y += Fg_y_soleil                         #* Soleil.sin_etoile
    
    return Fg_tot_y


#-------Calculs des coordonées de notre Asteroide-----#

coord_x_Asteroid = [asteroide_x_init]
coord_y_Asteroid = [asteroide_y_init]

for h in range(t):    

    #cette boucle permet d'ajouter t fois les valeurs initiales à notre asteroïde pour que il puisse rester 
    #pendant t jours à sa position initiale si on décide de le faire partir après t jours

    coord_x_Asteroid.append(asteroide_x_init)
    coord_y_Asteroid.append(asteroide_y_init)

def coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, j, t):

    #cette fonction calcule les coordonnées x et y de notre asteroïde selon la 2nde loi de newton

    for i in range(t, j):
       
        condition_vitesse_initiale_x = Asteroid_crash_test.vitesse_x
        condition_vitesse_initiale_y = Asteroid_crash_test.vitesse_y

        Asteroid_position_x = ((Fg_totale_x(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * (((i-t)+1)**2/2)) + condition_vitesse_initiale_x * ((i-t)+1) + coord_x_Asteroid[0]                                                    #+ Asteroid_vitesse_x * (i+1) + coord_x_Asteroid[i] 
        Asteroid_position_y = ((Fg_totale_y(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * (((i-t)+1)**2/2)) + condition_vitesse_initiale_y * ((i-t)+1) + coord_y_Asteroid[0]                                                      #+ Asteroid_vitesse_y * (i+1) + coord_y_Asteroid[i] 

        coord_x_Asteroid.append(Asteroid_position_x)
        coord_y_Asteroid.append(Asteroid_position_y)

    return np.array(coord_x_Asteroid), np.array(coord_y_Asteroid)

nb_coord_asteroid_cree = 60000

coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, nb_coord_asteroid_cree, t)

Asteroid_crash_test.coord_x = coord_x_Asteroid 
Asteroid_crash_test.coord_y = coord_y_Asteroid

print("Aquisition des coordonnées de notre Asteroid = ok !")


#----fonctions permettant de gérer la collision ou la sortie du système solaire----#


def distance_asteroid_planete(x_asteroid, y_asteroid, x_planete, y_planete):
    distance_A_P = np.sqrt((x_asteroid - x_planete)**2 + (y_asteroid - y_planete)**2)
    return distance_A_P

def collision(distance, rayon, name):
    global boom
    if distance < (rayon * 200): 
        boom = True                                                  
        print("collision avec", name)
        plt.text(4000000, 8000000, 'Collision avec ' + name, color = 'red', fontsize = 15)
        #return anim.event_source.stop()

def exit_solar_syst(coord_x, coord_y):
    global out
    marge = 100000
    if coord_x < x_min - marge or coord_x > x_max + marge or coord_y < y_min - marge or coord_y > y_max + marge:
        out = True
        print("sortie de l'asteroide du systeme solaire")
        plt.text(3600000, 8000000, "Asteroid is out of solar system", color = 'red', fontsize = 15)
        


#----fonctions de mise en mouvement des astres-----#



def run_animation():

    #cette fonction permet d'animer notre systeme solaire

    anim_running = True
    jour = 0
    
    def onClick(event):

        #cette fonction permet de mettre en pause l'animation suite à un clic sur la fenêtre matplotlib

        nonlocal anim_running
        if anim_running:
            anim.event_source.stop()
            anim_running = False
        else:
            anim.event_source.start()
            anim_running = True
            
    def init():
        pass

    def anim_astre(i):

        global boom, out 
        nonlocal anim_running, jour

        if i != 0:
            jour.remove()
        jour = ax.annotate("jour n° " + str(i), xy=(150, 60), xycoords = 'figure points', zorder=12)        # xycoords = 'figure points' => Points from the lower left of the figure  

        Asteroid_crash_test_plt.set_data(Asteroid_crash_test.coord_x[i], Asteroid_crash_test.coord_y[i])
        Asteroid_line.set_data(Asteroid_crash_test.coord_x[:i], Asteroid_crash_test.coord_y[:i])
        for j in range(len(list_plot_planete)):
            list_plot_planete[j].set_data(list_planete[j].coord_x[i], list_planete[j].coord_y[i])
            distance_A_P = distance_asteroid_planete(Asteroid_crash_test.coord_x[i], Asteroid_crash_test.coord_y[i], list_planete[j].coord_x[i], list_planete[j].coord_y[i])
            collision(distance_A_P, list_planete[j].rayon_collision, list_planete[j].name)
            if boom:
                return anim.event_source.stop()
        collision(distance_A_P, Soleil.rayon_collision, Soleil.name)
        exit_solar_syst(Asteroid_crash_test.coord_x[i], Asteroid_crash_test.coord_y[i])    
        if out:
            return anim.event_source.stop()

        return Asteroid_crash_test_plt, Asteroid_line, list_planete                
    
    fig.canvas.mpl_connect('button_press_event', onClick)
    anim = animation.FuncAnimation(fig, anim_astre, frames = Neptune.nb_frame ,init_func = init, interval = interval_time, blit = False, repeat = True)



run_animation()



#----différentes informations à afficher sous forme de texte sur notre animation-----#

if asteroide_x_init < 5000000:
    plt.text(6650000, 1200000, "valeurs initiales de la simulation: ", color = 'red', fontsize = 10, weight = "bold")
    plt.text(6700000, 1000000, "-coordonnée x de notre l'Asteroid: " + str(Asteroid_crash_test.coord_x_init), color = 'red', fontsize = 10)
    plt.text(6700000, 800000, "-coordonnée y de notre l'Asteroid: " + str(Asteroid_crash_test.coord_y_init), color = 'red', fontsize = 10)
    plt.text(6700000, 600000, "-vitesse en x: " + str(Asteroid_crash_test.vitesse_x), color = 'red', fontsize = 10)
    plt.text(6700000, 400000, "-vitesse en y: " + str(Asteroid_crash_test.vitesse_y), color = 'red', fontsize = 10)
    plt.text(6700000, 200000, "-nombre de jours avant lancement: " + str(Asteroid_crash_test.t), color = 'red', fontsize = 10)
else:
    plt.text(100000, 1200000, "valeurs initiales de la simulation: ", color = 'red', fontsize = 10, weight = "bold")
    plt.text(99500, 1000000, "-coordonnée initiale x de notre l'Asteroid: " + str(Asteroid_crash_test.coord_x_init), color = 'red', fontsize = 10)
    plt.text(99500, 800000, "-coordonnée initiale y de notre l'Asteroid: " + str(Asteroid_crash_test.coord_y_init), color = 'red', fontsize = 10)
    plt.text(99500, 600000, "-vitesse intiale en x: " + str(Asteroid_crash_test.vitesse_x), color = 'red', fontsize = 10)
    plt.text(99500, 400000, "-vitesse intiale en y: " + str(Asteroid_crash_test.vitesse_y), color = 'red', fontsize = 10)
    plt.text(99500, 200000, "-nombre de jours avant lancement: " + str(Asteroid_crash_test.t), color = 'red', fontsize = 10)



#-----caractéristiques de notre figure-----#

plt.title("Asteroid in solar system simulation")
plt.grid(alpha = 0.2)


# placement de la légende en dessous du graphique

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)

# plot du repère x, y

plt.arrow(9000000, 9000000, 440000, 0, head_width = 150000, head_length = 150000, fc = 'k', ec = 'r' )      #flèche de l'axe des x
plt.arrow(9000000, 9000000, 0, 500000, head_width = 100000, head_length = 200000, fc = 'k', ec = 'r' )      #flèche de l'axe des y
plt.text(9500000, 8800000, "x", color = 'red', fontsize = 6)
plt.text(8850000, 9600000, "y", color = 'red', fontsize = 6)

# affichage du graphique

plt.show()

