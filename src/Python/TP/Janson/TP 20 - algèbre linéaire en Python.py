#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction des Travaux Pratiques : 
    TP 20 - algèbre linéaire en Python.
"""


import numpy as np
import numpy.linalg as al


def resolution(A: np.array, Y: np.array) -> np.array :
    '''
    Renvoie la matrice X tq : AX = Y. (Pour A carré inversible)
    
    '''
    return al.solve(A, Y)


def verification(A: np.array, X: np.array, Y: np.array) -> bool :
    '''
    Renvoie vrai si X est bien la solution approché de : AX = Y.
    
    '''
    return np.allclose(np.dot(A, X), Y)

        
def noyau(A: np.array) -> list :
    '''
    Utilisation de la décomposition en valeur singulière pour trouver le Ker de A.

    '''
    U, S, V = al.svd(A)
    p, n = A.shape
    noyau: list = []
    for k in range(len(S)) :
        if S[k] == 0 :
            L = np.array([V[k, :]])
            noyau.append(L.transpose())
    if p < n :
        for k in range(p, n) :
            L = np.array([V[k, :]])
            noyau.append(L.transpose())
    return noyau
    
        
def pseudo_inverse(A: np.array) -> np.array :
    '''
    Renvoie le pseudo inverse de A à partir de sa décomposition 
    en valeur singulière.
    
    '''
    U, S, V = al.svd(A)
    p, n = A.shape

    S_plus = np.zeros((n, p))
    for i in range(len(S)) :
        if S[i] > 1e-10 :
            S_plus[i, i] = 1 / S[i]
    
    A_pseudo = np.dot(np.dot(np.transpose(V), S_plus), np.transpose(U))
    return A_pseudo
    

def test() -> None :
    
    # Matrice non inversible : Comment résoudre AX = Y quand A n'est pas inversible ou rectangulaire ?
    A = np.array( [ [ 3 , 1, -5,1, -12 ] , [ 0 , 5, 0, 0, 3 ], [4, -5, 0, 3, 0], [6,-1,5,-3,-5] ] )
    Y = np.array( [ [ 6 ] , [ 15 ], [2], [0] ] )
    
    p, n = A.shape
    rank = al.matrix_rank(A)
    if rank < n :
        v = np.array([[225], [-105], [-401], [-475], [175]])
        print(np.dot(A, v))
        print(f"A est de rang {rank} != {n}, donc A n'est pas inversible. Donc, Ker(A) !=  ∅")
        print(noyau(A))
    else :
        X = resolution(A, Y)
        print(X)
        print(verification(A, X, Y))
    
    # Solution : pseudo-inverse de Moore-Penrose. (A+ Y)
    print(verification(A, np.dot(pseudo_inverse(A), Y), Y))
   

test()