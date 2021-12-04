# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:40:23 2021

@author: Romeo Rouzier
"""

from Projet_prog_ba3 import asteroide_coor
import math

asteroide.genfromtext(coor_x, coor_y)


planetes = [Mercure, Venus, Terre, Mars,Jupiter, Saturne, Uranus, Neptune]

def collision (planete.x, planete.y):
    delta_planete = []
    for i in range (0, 8):
        distance_x = planete[i+1].x- planete[i].x
        distance_y = planete[i+1].y- planete[i].y
        
        distance = sqrt(distance_x**2 + distance_y**2)
        delta_planete.append(distance)
        
    return delta_planete
    
    
for i in range len(planetes) :
    if asteroide[x] + delta_planete[i] = planetes[i][x] and asteroide[y] = planetes[i][y] :
        print("Le crash")
    else :
        if (asteroide[x] <0 or asteroide[x]>10000) or (asteroide[y]<0 or asteroide[y] >10000) :
            print("asteroide ne touche pas de planete")
        else :
            asteroide[x] = asteroide[x+1]
            asteroide[y] = asteroide[y+1]
        

"""
while i < 100 :
    animate(asteroide) = 0 
    i += 1
"""