import numpy as np


nom_planètes = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune']

def planètes(nom_planète):

    nom_planète = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_' + nom_planète + '.csv', delimiter = ',', dtype = None)
    x = nom_planète[:, 0]
    y = nom_planète[:, 1]
    return nom_planète, x, y


Mercure, x_Mercure, y_Mercure = planètes(nom_planètes[0])
Venus, x_Venus, y_Venus = planètes(nom_planètes[1])
Terre, x_Terre, y_Terre = planètes(nom_planètes[2])
Mars, x_Mars, y_Mars = planètes(nom_planètes[3])
Jupiter, x_Jupiter, y_Jupiter = planètes(nom_planètes[4])
Saturne, x_Saturne, y_Saturne = planètes(nom_planètes[5])
Uranus, x_Urnaus, y_Uranus = planètes(nom_planètes[6])
Neptune, x_Neptune, y_Neptune = planètes(nom_planètes[7])



print(len(x_Neptune))



