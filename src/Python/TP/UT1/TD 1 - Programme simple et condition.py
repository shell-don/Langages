#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction du TD : 
    Programmation - TD 1 - Programme simple et condition.
"""


import math as m


def absolue(x: int) -> int :
    '''
    Fonction valeur absolue sans abs.
    
    '''
    if x < 0 :
        return -x
    else :
        return x
    

def egaux_ou_plus_grand(x: int, y: int) -> any :
    '''
    Renvoie les deux nombres (tuple) s'ils sont égaux,
    le plus grand des deux s'ils sont !=.
    
    '''
    if x == y :
        return x, y
    else :
        return max(x, y)
    

def compris_entre(a: int, b: int, c: int) -> bool :
    '''
    Vraie si c appartient à [a, b], faux sinon.
    
    '''
    if a <= c and c <= b :
        return True
    else :
        return False
    
    
def trois_condition(a: int, b: int, c: int, d: int) -> bool :
    '''
    Vraie si les trois conditions sont vérifié :
        - Le premier chiffre a pour valeur 1 ou 2.
        - Le quatrième chiffre a pour valeur 1 ou 2.
        - Les deuxième et troisième chiffres sont identiques.
    
    '''
    if (a == 1 or a == 2) and (d == 1 or d == 2) and (b == c) :
        return True
    else :
        return False
    
    
def angle_CAB(A: tuple, B: tuple, C: tuple) -> float :
    '''
    Renvoie l'angle en radians (converti en degres) entre les vecteurs AB et AC. 
    Prend en paramètre les coordonnées de chaque point.

    '''
    AB = [b-a for a, b in zip(A, B)]
    AC = [c-a for a, c in zip(A, C)]
    
    norme_AB = m.sqrt(AB[0]**2+AB[1]**2)
    norme_AC = m.sqrt(AC[0]**2+AC[1]**2)
    
    AB_scalaire_AC = AB[0]*AC[0] + AB[1]*AC[1]
    
    return m.degrees(m.acos(AB_scalaire_AC/(norme_AB*norme_AC)))


def test() -> None :
    
    print(absolue(-5))
    print(absolue(4))
    print("")
    
    print(egaux_ou_plus_grand(3, 3))
    print(egaux_ou_plus_grand(4, 3))
    print("")
    
    print(compris_entre(1, 5, 3))
    print(compris_entre(1, 5, 7))
    print("")
    
    print(trois_condition(1, 3, 3, 2))
    print(trois_condition(1, 2, 2, 4))
    print(trois_condition(1, 2, 3, 4))
    print(trois_condition(3, 2, 3, 4))
    print(trois_condition(5, 2, 3, 2))
    print("")
    
    print(angle_CAB((0,0), (3,0), (0,3)))


test()

