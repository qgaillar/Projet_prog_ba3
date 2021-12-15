import numpy as np


nom_planètes = ['planete_Mercure', 'planete_Venus', 'planete_Terre', 'Planete_Mars', 'planete_Jupiter', 'planete_Saturne', 'planete_Uranus', 'planete_Neptune', 'Asteroide']



def planètes(planète):
    nom_planète = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/' + planète + '.csv', delimiter = ',', dtype = None)
    x = nom_planète[:, 0]
    y = nom_planète[:, 1]
    nb_frame = len(nom_planète)

    return nom_planète, x, y, nb_frame

print("Modelisation in process...")

Mercure, x_Mercure, y_Mercure, frame_Mercure = planètes(nom_planètes[0])
Venus, x_Venus, y_Venus, frame_Venus = planètes(nom_planètes[1])
Terre, x_Terre, y_Terre, frame_Terre = planètes(nom_planètes[2])
Mars, x_Mars, y_Mars, frame_Mars = planètes(nom_planètes[3])
Jupiter, x_Jupiter, y_Jupiter, frame_Jupiter = planètes(nom_planètes[4])
Saturne, x_Saturne, y_Saturne, frame_Saturne = planètes(nom_planètes[5])
Uranus, x_Urnaus, y_Uranus, frame_Uranus = planètes(nom_planètes[6])
Neptune, x_Neptune, y_Neptune, frame_Neptune = planètes(nom_planètes[7])
Asteroide_w_a, x_Asteroide_w_a, y_Asteroide_w_a, frame_Asteroide_w_a = planètes(nom_planètes[8]) #Asteroide_without_attraction

print("Aquisiton des coordonnées de planètes = ok !")

Rayon_collision_planete = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/Rayon_planete_collision.csv', delimiter = ',', dtype = None)
Rayon_collision_planete = np.append(Rayon_collision_planete, 1000) #dernier rayon = rayon arbitraire pour le soleil


#print(len(Rayon_collision_planete))

données_initiales_Asteroid = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/valeur_init.csv', delimiter = ',', dtype = None)
x_Asteroid_init = données_initiales_Asteroid[0]
y_Asteroid_init = données_initiales_Asteroid[1]
angle_init = données_initiales_Asteroid[2]
V0_init = données_initiales_Asteroid[3]
nb_jour_lancement_init = int(données_initiales_Asteroid[4])




