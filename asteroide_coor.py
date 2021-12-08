# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:22:12 2021

@author: Romeo Rouzier
"""

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
            valeur = input("Mettre un nombre entre 0 et 10000000   ")
        else :
            break 

    valeur_int = int(valeur)
    
    while valeur_int < 0 or valeur_int >10000000 :
        print("La valeur n'est pas dans notre plot  ")
        valeur_int = int(input("Mettez un nombre entre 0 et 10000000  "))
    print(valeur_int)
    return valeur_int

