import numpy as np


nom_planètes = ['Mercure1', 'Venus1', 'Terre1', 'Mars1', 'Jupiter1', 'Saturne1', 'Uranus1', 'Neptune1', 'Asteroide0']



def planètes(nom_planète):

    nom_planète = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_' + nom_planète + '.csv', delimiter = ',', dtype = None)
    x = nom_planète[:, 0]
    y = nom_planète[:, 1]
    nb_frame = len(nom_planète)

    return nom_planète, x, y, nb_frame


Mercure, x_Mercure, y_Mercure, frame_Mercure = planètes(nom_planètes[0])
Venus, x_Venus, y_Venus, frame_Venus = planètes(nom_planètes[1])
Terre, x_Terre, y_Terre, frame_Terre = planètes(nom_planètes[2])
Mars, x_Mars, y_Mars, frame_Mars = planètes(nom_planètes[3])
Jupiter, x_Jupiter, y_Jupiter, frame_Jupiter = planètes(nom_planètes[4])
Saturne, x_Saturne, y_Saturne, frame_Saturne = planètes(nom_planètes[5])
Uranus, x_Urnaus, y_Uranus, frame_Uranus = planètes(nom_planètes[6])
Neptune, x_Neptune, y_Neptune, frame_Neptune = planètes(nom_planètes[7])
#Asteroide, x_Asteroide, y_Asteroide, frame_Asteroide = planètes(nom_planètes[8])








