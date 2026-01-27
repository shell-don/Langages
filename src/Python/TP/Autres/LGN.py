#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
    Illustration de lois de probabilités.
"""


import numpy
import matplotlib.pyplot as plt


def loi_des_grands_nombres() -> None :
    '''
    Montre la convergence en probabilité de 100 000 VA suivant la loi Bêta.
    Ici la d(x) = 1, donc la loi bêta est identique à la loi U([[0, 1]])

    '''
    a, b = 1, 1
    N = 100_000

    samples = [numpy.random.beta(a, b) for _ in range(N)]

    moyennes = []
    somme_cumulee = 0
    for i in range(1, N + 1):
        somme_cumulee += samples[i - 1]
        moyennes.append(somme_cumulee / i)

    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(moyennes, label="Moyenne empirique cumulé")
    plt.axhline(y=a/(a+b), color='r', linestyle='--', label="Espérance théorique")
    plt.xlabel("n", fontsize=8)
    plt.ylabel("Moyenne empirique", fontsize=8)
    plt.title("Loi des Grands Nombres", fontsize=12)
    plt.legend()
    plt.show()
    return


