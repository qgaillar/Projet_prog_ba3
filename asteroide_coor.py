# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:22:12 2021

@author: Romeo Rouzier
"""
import random

def valeur_coor():
    valeur = input("Quelle est la coordonnée voulue   ")
    
    try:
        int(valeur)
        it_is = True
    except ValueError:
        it_is = False
    
    while it_is != True :
        try:
            int(valeur)
            it_is = True
        except ValueError:
            it_is = False
        if it_is == False:
            print("Il faut mettre un chiffre et non une suite de caractères")
            valeur = input("Mettre un nombre entre 0 et 1000000   ")
        else :
            break 

    valeur_int = int(valeur)
    
    while valeur_int < 0 or valeur_int >1000000 :
        print("La valeur n'est pas dans notre plot  ")
        valeur_int = int(input("Mettez un nombre entre 0 et 1000000  "))
    print(valeur_int)
    return valeur_int


x = valeur_coor ()   
y = valeur_coor ()

asteroide_x = int(x)
asteroide_y = int(y)

while (asteroide_x >100000 and asteroide_x < 900000) and (asteroide_y > 100000 and asteroide_y < 900000 != True):
    print("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 100000 ou 900000 et 1000000")
    y = valeur_coor()
    asteroide_y = int(y)
print("c est juste le boss")


list_coor_x = []  
list_coor_y = [] 

     
vitesse_asteroide_x = random.randrange(-20, 20, 1)        
#print(vitesse_asteroide_x)
vitesse_asteroide_y = random.randrange(-20, 20, 1)
"""
for i in range 
coor_finale_x += x + vitesse_asteroide_x
coor_finale_y += y + vitesse_asteroide_y
"""
