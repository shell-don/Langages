#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction du TD : 
    Programmation - TD 5 - tableaux.
"""


def nb_valeurs_positive(tableau: list) -> int :
    '''
    Renvoie le nombre de valeurs positives ou nulles dans le tableau.
    
    '''
    c: int = 0
    for x in tableau :
        if x >= 0 : 
            c += 1
    return c


def sequence(sequence: tuple, tableau: list) -> int :
    '''
    Renvoie la position où la séquence de la forme (a,b,c) débute. -1 si elle n'est pas présente.

    '''
    a, b, c = sequence
    for i,x in enumerate(tableau[0:len(tableau) -2]) :
        if a == tableau[i] and b == tableau[i+1] and c == tableau[i+2] :
            return i
    return -1


def nb_appartient1(a: int, tableau: list) -> bool :
    '''
    Renvoie vraie si a appartient à un tableau de nombres. (avec in)

    '''
    if len(tableau) == 0 :
        return False
    else :
        return a in tableau


def nb_appartient2(a: int, tableau: list) -> bool :
    '''
    Renvoie vraie si a appartient à un tableau de nombres. (sans in)

    '''
    if len(tableau) == 0 :
        return False
    for x in tableau :
        if a == x :
            return True 
    return False 
    
    
def nb_true(tableau: list) -> int :
    '''
    Renvoie le nombre de True dans le tableau de booleen "tableau".
    
    '''
    return tableau.count(True)


def nb(tableau: list, X: any) -> int :
    '''
    Renvoie le nombre de X dans le tableau "tableau".
    
    '''
    return tableau.count(X)
    

def phrase_correct(phrase: list) -> any :
    '''
    Renvoie vraie si la phrase est syntaxiquement correcte 
    ie si elle est de la forme article + nom + verbe. (donné)

    '''
    articles: list = ["le", "la", "les", "des", "un", "une"]
    nom: list = ["vache", "chien", "chat", "canard"]
    verbe: list = ["aboyer", "caqueter", "miauler", "mugir"]
    
    correct: list = ["article", "nom", "verbe"]
    structure: list = []
    
    for i,x in enumerate(phrase) :
        if x in articles :
            structure.append("article")
        elif x in nom :
            structure.append("nom")
        elif x in verbe :
            structure.append("verbe")
        else :
            return f"Mot inconnu en position {i+1}."
    if structure == correct :
        return True 
    else :
        return "Mot mal placé."


def test() -> bool :
    
    assert nb_valeurs_positive([-2,4,9,1,-4,-6]) == 3, "Échec test 1 : nb_valeurs_positive()"
    assert nb_valeurs_positive([]) == 0, "Échec test 2 : nb_valeurs_positive()"
    
    assert sequence((1,2,3), [3,5,1,3,1,2,3]) == 4, "Échec test 3 : sequence()"
    
    assert nb_appartient1(3, [1,5,3,6]), "Échec test 4 : nb_appartient1()"
    assert not nb_appartient1(3, [1,5,2,6]),"Échec test 5 : nb_appartient1()"
    assert not nb_appartient1(3, []),"Échec test 6 : nb_appartient1()"
    assert nb_appartient2(7, [1,2,6, 7]),"Échec test 7 : nb_appartient2()"
    assert not nb_appartient2(7, [1,2,6, 3]), "Échec test 8 : nb_appartient2()"
    assert not nb_appartient2(7, []), "Échec test 9 : nb_appartient2()"

    assert nb_true([False, True, True, True]) == 3, "Échec test 10 : nb_true()"
    
    assert nb([False, True, True, True], False) == 1, "Échec test 11 : nb()"
    
    assert phrase_correct(["les", "chien", "aboyer"]), "Échec test 12 : phrase_correct()"
    assert phrase_correct(["aboyer", "chien", "les"]) == "Mot mal placé.", "Échec test 13 : phrase_correct()"
    assert phrase_correct(["aboyer", "loup", "les"]) == "Mot inconnu en position 2.", "Échec test 14 : phrase_correct()"
    
    return True


test()

