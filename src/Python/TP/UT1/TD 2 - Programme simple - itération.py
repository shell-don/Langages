#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction du TD : 
    Programmation - TD 2 - Programme simple - iteration.
"""


import numpy as np


def suite(n: int) -> list :
    '''
    Renvoie une liste des n-première valeurs de 2^n.

    '''
    return [2**k for k in range(n)]


def compris_entre_1_et_9(x: int) -> bool :
    '''
    Vraie si x appartient à [1, 9].

    '''
    if 1 <= x and x <= 9 :
        return True
    else :
        return False
    
    
def fibonacci(n: int) -> int :
    '''
    Renvoie la n-ime valeur de la suite de Fibonacci.
    
    '''
    if n == 0 :
        return 0
    elif n == 1 :
        return 1 
    else :
        return n + fibonacci(n-1) 


def suite_fibonacci(n: int) -> list :
    '''
    Renvoie la liste des n-premier nombre de Fibonacci.
    
    '''
    return [fibonacci(x) for x in range(n)]


def somme_et_moyenne(n: int) -> tuple :
    '''
    Renvoie la somme et la moyenne de n entiers entré par l'utilisateur.

    '''
    A = [int(input()) for x in range(n)]
    return (sum(A), float(np.mean(A)))


def losange() -> None :
    '''
    Affiche un losange.

    '''
    taille = 5
    # Partie supérieure
    for i in range(taille):
        espaces = " " * (taille - i - 1)
        etoiles = "*" * (2 * i + 1)
        print(espaces + etoiles + espaces)
    
    # Partie inférieure
    for i in range(taille - 2, -1, -1):
        espaces = " " * (taille - i - 1)
        etoiles = "*" * (2 * i + 1)
        print(espaces + etoiles + espaces)
        

def divisible_par_5 (a: int, b: int) -> list :
    '''
    Renvoie la liste des nombres divisible par 5 sur l'intervalle [a, b].

    '''
    return [x for x in range(a, b) if x%5 ==0]


def test() -> None :
    
    print(suite(5))
    print("")
    
    print(compris_entre_1_et_9(6))
    print(compris_entre_1_et_9(9))
    print(compris_entre_1_et_9(10))
    print("")
    
    print(suite_fibonacci(16))
    print("")

    print(somme_et_moyenne(2))
    
    losange()
    print("")
    
    print(divisible_par_5(5, 20))
    
    
test()
