#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author : Mathis Pigassou
Chapitre 22 d'Exos-1 :
Création d'un modèle simple de Bitcoin pour comprendre le principe de preuve de travail.
'''


from random import randint
import time


# Introduction, Preuve de travail : un problème difficile à résoudre mais facileà vérifier.


def verification(x: int, y: int, p: int) -> bool :
    '''
    Renvoie « vrai » si x est bien solution du problème
    x^2 = y (mod p) et « faux » sinon. (Simple)
    
    '''
    if (x**2 % p) == (y % p):
        return True
    else :
        return False
    
    
def racine(y: int, p: int) -> int :
    '''
    Renvoie une solution x du problème x^2 = y (mod p),
    pour y et p donné ou None s’il n’y a pas de solution. (Difficile)

    '''
    for x in  range(100_000_000) :
        if (x**2 % p) == (y % p) :
            return x
    

def racine_approchee(y: int, p: int, epsilon: int) -> int :
    '''
    Renvoie une solution approchée à epsilon près de x^2 = y (mod p). (Difficulté ajusté)
   
    '''
    for x in range(p) :  
        if abs((x**2 % p) - (y % p))  <= epsilon :
            return x
    return -1 
    

# Outils pour les listes.


def addition(liste_1: list, liste_2: list ) -> list :
    '''
    Additionne terme àterme et modulo 100, les éléments 
    de deux listes de même longueur. (outil pour la fonction de hachage)

    '''
    # zip renvoie un tuple composé des éléments de même indice de chaques listes.
    return [(x + y) % 100 for x, y in zip(liste_1, liste_2)]
        

def est_plus_petit(liste_1: list, liste_2: int) -> bool :
    '''
    renvoie « vrai » lorsque liste_1 est plus petite que liste_2, faux sinon. 
    (outil pour la verification de la preuve de travail)
    '''
    return all(x <= y for x, y in zip(liste_1, liste_2))


def phrase_vers_liste(phrase: str) -> list :
    '''
    Convertit une chaîne de caractères en une liste
    d'entiers entre 0 et 99 et si besoin rajoute des zéros 
    devant afin que la liste ai la bonne taille (multiple de 6).
    Cette liste de chiffres sera notre message. 
    (outil pour le calcul d'une preuve de travail après transaction)

    '''
    liste = [ord(x) % 100 for x in phrase]
    reste = len(liste) % 128
    if reste != 0 :
        nombre_a_ajouter = 128 - reste
        liste = [0] * nombre_a_ajouter + liste
    return liste



# Fonction de hachage : créer une fonction de hachage.


def addition_interne(bloc: list) -> list :
    '''
    Pour un bloc de taille 6, additionne certains éléments.
    Les éléments d'indice pair sont conservés, 
    les éléments d'indice impair sont remplacés par la somme 
    de l'élément et de celui qui le précède.
    
    '''
    return [x if i % 2 == 0 else x + bloc[i - 1] for i, x in enumerate(bloc)]


def multiplication_interne(bloc: list) -> list :
    '''
   Multiplication des termes, forme : bloc*nb_premier + 1.

    '''
    return [(x*i)+1 for x, i in zip(bloc, [7, 11, 13, 17, 19, 23, 15, 67])]


def permutation_circulaire_gauche(bloc: list) -> list :
    ''' 
    Permute les éléments de la liste de 1 vers la gauche.
   
    '''
    return [bloc[i+1] if i == len(bloc)-1 else bloc[0] for i, x in enumerate(bloc)]


def permutation_circulaire_droite(bloc: list) -> list :
    ''' 
    Permute les éléments de la liste de 1 vers la droite.
   
    '''
    return [bloc[-1] if i == 0 else bloc[i-1] for i, x in enumerate(bloc)]


def modulo_100(bloc: list) -> list :
    '''
    Renvoie le bloc modulo 100.

    '''
    return [x % 100 for x in bloc]


def un_tour(bloc: list) -> list :
    '''
    Renvoie la transformation du bloc après certaines transformations.
    - addition
    - multiplication
    - permutation
    - modulo 100

    '''
    return modulo_100(permutation_circulaire_droite(multiplication_interne(addition_interne(bloc))))


def dix_tours(bloc: list) -> list :
    '''
    Renvoie le bloc après 10 tours sur un bloc de taille 6.

    '''
    for _ in range(10) : 
        bloc = un_tour(bloc)
    return bloc


def hachage(liste: list) -> list :
    '''
    Revoie l'empreinte d'une liste de nombres (message) multiple de 6.

    '''
    blocs = [liste[i:i + 8] for i in range(0, len(liste), 8)]
    for i in range(len(blocs)-1) :
        blocs[i] = dix_tours(blocs[i])
        blocs[i+1] = addition(blocs[i], blocs[i+1])
    return dix_tours(blocs[-1])
    
print(hachage(phrase_vers_liste("je m'appellle françoisss")))

# Preuve de travail - Minage : 
# il s'agit de trouver un bloc preuve qui vérifie : hachage(liste + preuve) <= Max pour Max et liste donnés.


def verification_preuve_de_travail(liste: list, preuve: list, maxi: list) -> bool :
    '''
    Renvoie vrai si la solution preuve proposée convient pour liste. (Facile)

    '''
    if est_plus_petit(hachage(liste+preuve) , maxi) :
        return True
    else :
        return False


def preuve_de_travail(liste: list, maxi: list) -> list :
    '''
    Cherche un bloc preuve solution à notre problème pour la liste donnée. (Difficile)
    Pour le bitcoin, ceux qui calculent des preuves de travail sont appelés les mineurs.
    La difficulté du problème est ajustée de sorte que le temps de calcul soit d'environ 10 
    minutes.

    '''
    preuve = [randint(0, 100) for x in range(6)]
    while not est_plus_petit(hachage(liste+preuve) , maxi) :
        preuve = [randint(0, 100) for x in range(6)]
    return preuve


def test_minage() -> None :
    
    # Recherche d'une solution (minage) de difficulté moyen :  [0,0,5]
    print(preuve_de_travail([0, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1], [0,0,5]))
    # Après quelques secodes un résultat est trouvé: [95, 88, 44, 24, 21, 35]
    print(verification_preuve_de_travail([0, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1], [95, 88, 44, 24, 21, 35], [0,0,5]))
    # Cela est bien une solution.


# Bitcoins : créer un livre de compte (appelé blockchain pour le bitcoin) qui enregistre toutes les transactions.


Livre: list = [ [0,0,0,0,0,0] ]


def ajout_transaction(transaction: str) -> None :
    '''
    Ajoute la chaîne de caractères transaction à la liste Livre.

    '''
    global Livre
    
    Livre.append(transaction)
    
    
def cout_transaction() -> None :
    '''
    Ajoute une preuve de travail au Livre (Pour chaque transaction).

    '''
    global Livre
    
    transaction = phrase_vers_liste(Livre[-1])
    prec_preuve = Livre[-2]
    Livre.append(preuve_de_travail(prec_preuve+transaction, [0,0,5]))


def test_livre_de_compte() -> None :
    
    debut_chrono = time.time()

    ajout_transaction("Abel +35")
    cout_transaction()
    print(Livre)

    # Livre : [[0, 0, 0, 0, 0, 0], 'Abel +35', [83, 90, 51, 100, 39, 27]] 
    # (10.286720991134644 sec)

    fin_chrono = time.time()
    total_chrono = fin_chrono-debut_chrono
    print(total_chrono)


