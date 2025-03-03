#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
    Différentes courbes de densités et de masses suivant des lois de probabilités.
"""


import numpy as np
import matplotlib.pyplot as plt
import math


def lois_usuelles_de_VA_a_densite() -> None :
    '''
    Procédure traçant les densités de lois usuelles.

    '''
    x = np.linspace(0, 8, 100000)
    y_normale = [1/1*np.sqrt(math.pi*2)*math.exp(-1/2*pow((i-4)/1, 2)) for i in x]
    y_uniforme = [1/4 if (i >= 3 and i <= 5) else 0 for i in x ]
    y_expo1 = [0 if i < 0 else 2*math.exp(-2*i) for i in x]
    y_expo2 = [0 if i < 0 else 1*math.exp(-1*i) for i in x]
    y_expo3 = [0 if i < 0 else 0.5*math.exp(-0.5*i) for i in x]
    
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(x, y_normale, label='N(4, 1²)', color='royalblue', linewidth=2)
    plt.plot(x, y_uniforme, label='U([3, 5])', color='green', linewidth=2)
    plt.plot(x, y_expo1, label='E(2)', color='red', linewidth=2)
    plt.plot(x, y_expo2, label='E(1)', color='orange', linewidth=2)
    plt.plot(x, y_expo3, label='E(0.5)', color='yellow', linewidth=2)
    plt.xlabel("Valeurs", fontsize=10)
    plt.ylabel("Densités de probabilités", fontsize=10)
    plt.title("Densités de lois usuelles.", fontsize=12)
    
    plt.legend()
    plt.show()
    return

    
def lois_usuelles_de_VA_discrete() -> None :
    '''
    Procédure traçant les fonctions de masse de lois usuelles.
    
    '''
    x = [x for x in range(0,25)]
    y_poisson = [math.exp(-7)*(pow(7, i)/math.factorial(i)) for i in x]
    y_geometric = [0.5*pow(1-0.5, i-1) for i in x]
    y_uniform = [1/5 if i >= 23 and i <= 25 else 0 for i in x]
    y_binomial = [math.comb(25, i)*pow(0.7, i)*pow((1-0.7), 25-i) for i in x]
    y_bernoulli = [0.8 if i == 1 else (1 - 0.8 if i == 0 else 0) for i in x]

    plt.figure(figsize=(10, 6), dpi=300)
    plt.scatter(x, y_poisson, color='red', s=18, label='P(7)')
    plt.vlines(x, 0, y_poisson, colors='red', linestyles='dashed', alpha=0.35)
    plt.scatter(x, y_geometric, color='purple', s=18, label='G(0.5)')
    plt.vlines(x, 0, y_geometric, colors='purple', linestyles='dashed', alpha=0.35)
    plt.scatter(x, y_uniform, color='orange', s=18, label='U([23, 24])')
    plt.vlines(x, 0, y_uniform, colors='orange', linestyles='dashed', alpha=0.35)
    plt.scatter(x, y_binomial, color='green', s=18, label='B(25, 0.7)')
    plt.vlines(x, 0, y_binomial, colors='green', linestyles='dashed', alpha=0.35)
    plt.scatter(x, y_bernoulli, color='pink', s=18, label='B(0.8)')
    plt.vlines(x, 0, y_bernoulli, colors='pink', linestyles='dashed', alpha=0.35)
    plt.xlabel("Valeurs", fontsize=10)
    plt.ylabel("Masse", fontsize=10)
    plt.title("Fonction de masse de lois usuelles.", fontsize=12)

    plt.legend()
    plt.show()
    return


def loi_beta() -> None :
    '''
    Trace la densité 'd' sur ]0, 1[ suivant plusieurs paramètres.
    d : ]0, 1[ -> R
              x  - > ( x**(a-1)*(1-x)**(b-1) ) / B(a, b)
    avec B(a,b) la fonction bêta, a > 0 et b > 0.
    On a : B(a,b) =  ( Γ(a)* Γ(b) ) /  Γ(a + b)
    (area scaling sur [0, 2.7])

    '''
    x = np.linspace(0.0000000001, 0.9999999999, 100000)
    y_beta1 = [(pow(i, 0.5-1)*pow(1-i, 0.5-1) * math.gamma(0.5+0.5)) / math.gamma(0.5)*math.gamma(0.5) for i in x]
    y_beta2 = [(pow(i, 2-1)*pow(1-i, 5-1) * math.gamma(2+1)) / math.gamma(2)*math.gamma(5) for i in x]
    y_beta3 = [(pow(i, 1-1)*pow(1-i, 3-1) * math.gamma(1+3)) / math.gamma(1)*math.gamma(3) for i in x]
    y_beta4 = [(pow(i, 6-1)*pow(1-i, 0.7-1) * math.gamma(6+0.7)) / math.gamma(6)*math.gamma(0.7) for i in x]
    y_beta5 = [(pow(i, 2-1)*pow(1-i, 2-1) * math.gamma(2+2)) / math.gamma(2)*math.gamma(2) for i in x]
    y_beta6 = [(pow(i, 0.7-1)*pow(1-i, 6-1) * math.gamma(0.7+6)) / math.gamma(0.7)*math.gamma(6) for i in x]
    aire = np.trapz(y_beta1, x)
    y_beta1_normalise =  [i / aire for i in y_beta1] 
    aire = np.trapz(y_beta2, x)
    y_beta2_normalise =  [i / aire for i in y_beta2] 
    aire = np.trapz(y_beta3, x)
    y_beta3_normalise =  [i / aire for i in y_beta3] 
    aire = np.trapz(y_beta4, x)
    y_beta4_normalise =  [i / aire for i in y_beta4] 
    aire = np.trapz(y_beta5, x)
    y_beta5_normalise =  [i / aire for i in y_beta5] 
    aire = np.trapz(y_beta6, x)
    y_beta6_normalise =  [i / aire for i in y_beta6] 
    
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(x, y_beta1_normalise, label='a = b = 0.5', color='red', linewidth=2)
    plt.plot(x, y_beta2_normalise, label='a = 2, b = 5', color='green', linewidth=2)
    plt.plot(x, y_beta3_normalise, label='a = 1, b = 3', color='blue', linewidth=2)
    plt.plot(x, y_beta4_normalise, label='a = 6, b = 0.7', color='purple', linewidth=2)
    plt.plot(x, y_beta5_normalise, label='a = 2, b = 2', color='pink', linewidth=2)
    plt.plot(x, y_beta6_normalise, label='a = 0.7, b = 6', color='orange', linewidth=2)
    plt.ylim(0, 2.7)
    plt.xlabel("Valeurs", fontsize=8)
    plt.ylabel("Densité de probabilités", fontsize=8)
    plt.title("Densité de la loi bêta.", fontsize=12)

    plt.legend()
    plt.show()
    return


def loi_gamma() -> None :
    '''
    Trace la densité de la loi gamma suivant plusieurs paramètres.
    d : R+ -> R
        x -> (x**(k-1)*exp(-x/θ)) /  Γ(k) * θ**k
    avec k > 0 et θ > 0.
    (min-max scaling sur [0,1])
    
    '''
    x = np.linspace(0, 20, 100000)
    k, t = 1, 3.5
    y_gamma1 = [(pow(i, k-1)*math.exp(-i/t))/math.gamma(k)*pow(t,k) for i in x]
    max_gamma1 = max(y_gamma1)
    min_gamma1 = min(y_gamma1)
    k, t = 3, 1.0
    y_gamma2 = [(pow(i, k-1)*math.exp(-i/t))/math.gamma(k)*pow(t,k) for i in x]
    max_gamma2 = max(y_gamma2)
    min_gamma2 = min(y_gamma2)
    k, t = 3, 1.6
    y_gamma3 = [(pow(i, k-1)*math.exp(-i/t))/math.gamma(k)*pow(t,k) for i in x]
    max_gamma3 = max(y_gamma3)
    min_gamma3 = min(y_gamma3)
    k, t = 6, 1.1
    y_gamma4 = [(pow(i, k-1)*math.exp(-i/t))/math.gamma(k)*pow(t,k) for i in x]
    max_gamma4 = max(y_gamma4)
    min_gamma4 = min(y_gamma4)
    k, t = 3, 1.5 
    y_gamma5 = [(pow(i, k-1)*math.exp(-i/t))/math.gamma(k)*pow(t,k) for i in x]
    max_gamma5 = max(y_gamma5)
    min_gamma5 = min(y_gamma5)
    maxi = max(max_gamma1,max_gamma2, max_gamma3, max_gamma4, max_gamma5)
    mini = min(min_gamma1,min_gamma2, min_gamma3, min_gamma4, min_gamma5)
    y_gamma1_normalise = [1*((i-mini)/(maxi-mini)) for i in y_gamma1]
    y_gamma2_normalise = [1*((i-mini)/(maxi-mini)) for i in y_gamma2]
    y_gamma3_normalise = [1*((i-mini)/(maxi-mini)) for i in y_gamma3]
    y_gamma4_normalise = [1*((i-mini)/(maxi-mini)) for i in y_gamma4]
    y_gamma5_normalise = [1*((i-mini)/(maxi-mini)) for i in y_gamma5]

    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(x, y_gamma1_normalise, label='k = 1,  θ= 3.5', color='crimson', linewidth=2)
    plt.plot(x, y_gamma2_normalise, label='k = 3,  θ= 1.0', color='tan', linewidth=2)
    plt.plot(x, y_gamma3_normalise, label='k = 3,  θ= 1.6', color='sienna', linewidth=2)
    plt.plot(x, y_gamma4_normalise, label='k = 6,  θ= 1.1', color='forestgreen', linewidth=2)
    plt.plot(x, y_gamma5_normalise, label='k = 3,  θ= 1.5', color='darkgoldenrod', linewidth=2)
    plt.ylim(0, 1.0)
    plt.xlabel("Valeurs", fontsize=8)
    plt.ylabel("Densité de probabilités", fontsize=8)
    plt.title("Densité de la loi Gamma.", fontsize=12)
    
    plt.legend()
    plt.show()
    return


def loi_du_χ2() -> None :
    '''
    Trace la densité de la loi du khi-deux suivant plusieurs k. 
    (k loi normale centré réduite indépendante)
    d : R+ -> R
        x -> (1/2**k/2 ) / Γ(k/2)  *  x**(k/2)-1  * exp(-x/2)

    '''
    x = np.linspace(0, 10, 100000)
    k = 1
    y_khi1 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]
    k = 2
    y_khi2 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]
    k = 3
    y_khi3 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]
    k = 4
    y_khi4 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]
    k = 6
    y_khi5 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]
    k = 8
    y_khi6 = [(pow(1/2,k/2)/math.gamma(k/2)) * pow(i, (k/2)-1)*math.exp(-i/2) for i in x]

    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(x, y_khi1, label='k = 1', color='#004c6d', linewidth=2)
    plt.plot(x, y_khi2, label='k = 2', color='#287d7d', linewidth=2)
    plt.plot(x, y_khi3, label='k = 3', color='#6aae8b', linewidth=2)
    plt.plot(x, y_khi4, label='k = 4', color='#aacc76', linewidth=2)
    plt.plot(x, y_khi5, label='k = 6', color='#f3e55c', linewidth=2)
    plt.plot(x, y_khi6, label='k = 8', color='#ffe900', linewidth=2)

    plt.ylim(0, 0.5)
    plt.xlabel("Valeurs", fontsize=8)
    plt.ylabel("Densité de probabilités", fontsize=8)
    plt.title("Densité de la loi du χ2 .", fontsize=12)
    
    plt.legend()
    plt.show()
    return


def loi_des_grands_nombres() -> None :
    '''
    Montre la convergence en probabilité de 100 000 va suivant la loi Bêta.
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


loi_du_χ2()

