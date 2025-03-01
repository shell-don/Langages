#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction du TD : 
    Programmation - TD 6 - tableaux.
"""


import random
import math


def trouver(tab:list) -> any :
    '''
    Renvoie la première valeur dupliqué dans le tableau.
    
    '''
    L:list = []
    if len(tab) == 0 :
        return -1
    for x in tab :
        if x in L :
            return x
        else :
            L.append(x)
    return -1


def moyenne(tab: list) -> float :
    '''
    Renvoie la moyenne des valeurs du tableau.
    
    '''
    if len(tab) == 0 :
        return 0.0
    else :
        return (sum(tab)/len(tab))


def ecart_type(tab: list) -> float :
    '''
    Renvoie l'écart type d'une liste de valeurs.

    '''
    if len(tab) == 0 :
        return -1
    tab_carre: list = [pow(x,2) for x in tab]
    var: int = moyenne(tab_carre) - pow(moyenne(tab), 2)
    return pow(var, 1/2)

    
def dans_intervalle(valeur: float, moy: float, n: int, ecart_t: float) -> bool :
    '''
    Renvoie vrai si valeur est dans [moy - n*ecart_t, moy + n*ecart_t].

    '''
    if valeur >= moy - n*ecart_t and valeur <= moy + n*ecart_t :
        return True 
    else : 
        return False


def tab_dans_intervalle(tab: list, moy: float, n: int, ecart_t: float) -> any :
    '''
    Renvoie vrai si toutes les valeurs de tab sont dans [moy - n*ecart_t, moy + n*ecart_t]. 
    Sinon renvoi le nombre de valeurs n'étant pas dans l'intervalle

    '''
    tmp: int = 0
    if len(tab) == 0 :
        return -1
    for x in tab :
        if x >= moy - n*ecart_t and x <= moy + n*ecart_t :
            pass
        else :
            print(f"{x} n'est pas dans [{moy - n*ecart_t}, {moy + n*ecart_t}]")
            tmp += 1
    if tmp == 0 :
        return True
    else :
        return tmp


def proximite(L1: list, L2: list) -> float :
    '''
    Renvoie la proximité entre les deux listes.

    '''
    tmp: list = [pow(L1[i]-L2[i], 2) for i, x in enumerate(L1)]
    return pow(sum(tmp), 1/2)
    

def angle(L1: list, L2: list) -> float :
    '''
    Renvoie l'angle en radian de deux vecteurs (L1 et L2).
    Si les vecteurs sont de tailles différentes, 
    alors le plus grand vecteur est réduit au deuxième. (cf test 22)
    
    '''
    if len(L1) > len(L2) :
        _: int = len(L2)
    else :
        _: int = len(L1)
    
    scalaire: float = sum(L1[i]*L2[i] for i in range(_))
    norme_L1: float = math.sqrt(sum(x**2 for x in L1))
    norme_L2: float = math.sqrt(sum(x**2 for x in L2))
    
    if norme_L1 == 0 or norme_L2 == 0 or len(L1) == 0 or len(L2) == 0 :
        return -1
    else :
        cos_theta = scalaire / (norme_L1 * norme_L2)
        return round(math.degrees(math.acos(cos_theta)), 2)


def pourcent(L1: list, moy: float, n: int, ecart_t: float) -> float :
    '''
    Renvoie le pourcentage de valeurs comprise dans un intervalle.

    '''
    tmp: int = 0
    c: int = 0
    if len(L1) == 0 :
        return -1
    for x in L1 :
        if x >= moy - n*ecart_t and x <= moy + n*ecart_t :
            c += 1
        else :
            tmp += 1
    return (c/len(L1))*100


def suit_loi_normale(L1: list, e: float) -> bool :
    '''
    Renvoie vai si les valurs de L1 suivent une loi normale à epsilon près.

    '''
    if len(L1) == 0 :
        return -1
    
    moy: float = moyenne(L1)
    ecart_t: float = ecart_type(L1)
    n: int = 1
    
    if pourcent(L1, moy, n, ecart_t) >= 68.0 - e and pourcent(L1, moy, n, ecart_t) <= 68.0 + e :
        n += 1
        if pourcent(L1, moy, n, ecart_t) >= 95.0 - e and pourcent(L1, moy, n, ecart_t) <= 95.0 + e :
            n += 1
            if pourcent(L1, moy, n, ecart_t) >= 99.7 - e and pourcent(L1, moy, n, ecart_t) <= 99.7 + e :
                return True
            else :
                return False
        else :
            return False
    else :
        return False
    

def test() -> bool :
    
    assert trouver([1, 4, 5, 6, 4, 1]) == 4, "Échec test 1 : trouver()"
    assert trouver([1, 4, 5, 6, 1, 4]) == 1, "Échec test 2 : trouver()"
    assert trouver([1, 2, 3, 4, 5]) == -1, "Échec test 3 : trouver()"
    assert trouver([]) == -1, "Échec test 3 : trouver()"
    
    assert moyenne([0,10]) == 5.0, "Échec test 4 : moyenne()"
    assert moyenne([0,5]) == 2.5, "Échec test 5 : moyenne()"
    assert moyenne([]) == 0.0, "Échec test 6 : moyenne()"
    
    assert ecart_type([1,1,1,1]) == 0.0, "Échec test 7 : ecart_type()"
    assert ecart_type([]) == -1.0, "Échec test 8 : ecart_type()"
    
    assert dans_intervalle(3.23, 2.0, 3, 1.5) == True, "Échec test 9 : dans_intervalle()"
    assert dans_intervalle(-2.51, 2.0, 3, 1.5) == False, "Échec test 10 : dans_intervalle()"
    assert dans_intervalle(6.51, 2.0, 3, 1.5) == False, "Échec test 11 : dans_intervalle()"
    
    assert tab_dans_intervalle([2.5, 5, 2, 3.12], 2.0, 3, 1.5) == True, "Échec test 12 : tab_dans_intervalle()"
    assert tab_dans_intervalle([2.5, -5.5, 2, 7], 2.0, 3, 1.5) == 2, "Échec test 13 : tab_dans_intervalle()"    
    
    assert proximite([0, 0], [3, 4]) == 5.0, "Échec test 14 : norme()"
    assert proximite([1, 2, 3], [4, 5, 6]) == pow(27, 1/2), "Échec test 15 : norme()"
    assert proximite([10, 20, 30], [10, 20, 30]) == 0.0, "Échec test 16 : norme()"
    
    assert angle([1, 0], [0, 1]) == 90.0, "Échec test 17 : angle()"
    assert angle([1, 0], []) == -1, "Échec test 18 : angle()"
    assert angle([], [1]) == -1, "Échec test 19 : angle()"
    assert angle([], []) == -1, "Échec test 20 : angle()"
    assert angle([1,1], [2,2]) == 0.0, "Échec test 21 : angle()"
    assert angle([1, 0, 2], [0, 1]) == 90.0, "Échec test 22 : angle()"
    
    assert pourcent([1,2,3,4], 2.5, 1, 3.0) == 100.0, "Échec test 23 : pourcent()"
    assert pourcent([1,2,12,40], 2.5, 1, 3.0) == 50.0, "Échec test 24 : pourcent()"
    assert pourcent([-10,-20,12,40], 2.5, 1, 3.0) == 0.0, "Échec test 25 : pourcent()"
    assert pourcent([], 2.5, 1, 3.0) == -1, "Échec test 26 : pourcent()"
    
    assert suit_loi_normale([], 1.0) == -1, "Échec test 27 : suit_loi_normale()"
    liste_normale = [random.gauss(0, 1) for _ in range(1000000)]
    # plus le nombre de valeur est grand plus epsilon peut être petit.
    assert suit_loi_normale(liste_normale, 0.5) == True, "Échec test 28 : suit_loi_normale()"
    liste_uniforme = [random.uniform(-3, 3) for _ in range(1000)]
    assert suit_loi_normale(liste_uniforme, 2.5) == False, "Échec test 29 : suit_loi_normale()"
    
    return True


test()

