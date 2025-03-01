#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Mathis Pigassou
Correction du TD : 
    Programmation - TD 4 - Chaines.
"""


def nombre_mot(phrase: str) -> int :
    '''
    Renvoie  le nombre de mots apparaissant dans la chaîne de caractères 'phrase'.

    '''
    c: int = 1
    if len(phrase) == 0 :
        return 0
    for i in phrase :
        if i == ' ' :
            c +=1
    return c
        
    
def normalise(chaine: str) -> str :
    '''
    Renvoie la chaine normalisé,  tous les espaces en début et fin de chaine sont enlevés, 
    et le mot à l’intérieur de celui-ci est converti en minuscule. (manque)
    
    '''
    chaine = ['' if x == ' ' else x for x in chaine]
    chaine = ''.join(chaine)
    return chaine.lower()


def comparaison(mot1: str, mot2: str) -> bool :
    '''
    Renvoie vrai si les deux mots sont les mêmes. Ignore les espaces et les majuscules.
    
    '''
    mot1 = normalise(mot1)
    mot2 = normalise(mot2)

    mot1 = [x for x in mot1]
    mot2 = [x for x in mot2]
    
    if len(mot1) !=  len(mot2) :
        return False
    
    c: int = 0
    for i, x in enumerate(mot1) :
        if x == mot2[i] :
            c += 1
    if c == len(mot1) and c == len(mot2) :
        return True
    else :
        return False


def verifier(mot: str) -> bool :
    '''
    Renvoie vrai si le mot correspond aux règles du mastermind :
        - taille de 4 lettres
        - composé de A, B, C, D, E, F.
        
    '''
    if len(mot) != 4 :
        return False
    mot = [x for x in mot]
    for x in mot :
        if x != "A" and x != "B" and x != "C" and x != "D" and x != "E" and x != "E" and x != "F"  :
            return False
    return True


def lettre_appartient(lettre: str, mot: str) -> bool :
    '''
    Renvoie vrai si la lettre est dans le mot.
    
    '''
    for i in mot :
        if lettre == i :
            return True
    return False


def bonne_place(lettre: str, place: int, mot: str) -> bool :
    '''
    Renvoie vrai si la lettre appartient ET est à la bonne place dans le mot ie le bon index.

    '''
    index: int = 0
    for i, x in enumerate(mot) :
        if x == lettre :
            index = i
            break
    if lettre_appartient(lettre, mot) and index == place :
        return True
    else :
        return False
    
    
def indice(mot_deviner: str, mot_propose: str) -> str :
    '''
    Renvoie un indice de la forme :
        O : Correct
        M : Correct mais mal placé
        N : incorrect 

    '''
    indice = []
    mot_propose = list(mot_propose)  
    mot_deviner = list(mot_deviner)

    # Identifier les lettres bien placées
    for i in range(len(mot_propose)):
        if mot_propose[i] == mot_deviner[i]:
            indice.append("O")
            mot_deviner[i] = None
            mot_propose[i] = None  
        else:
            indice.append("") 

    # Identifier les lettres mal placées
    for i in range(len(mot_propose)) :
        if mot_propose[i] is not None and mot_propose[i] in mot_deviner :
            indice[i] = "M"  
        elif mot_propose[i] is not None :
            indice[i] = "N"

    return "".join(indice)


def nb_lettre_correct(mot_deviner: str, mot_propose: str) -> int :
    '''
    Renvoie le nombre de lettres correctement devinées et bien placées.
    
    '''
    c: int = 0
    indic: str = indice(mot_deviner, mot_propose)
    for x in indic :
        if x == "O" :
            c += 1
    return c


def nb_lettre_mal_placé(mot_deviner: str, mot_propose: str) -> int :
    '''
    Renvoie le nombre de lettres correctement devinées mais mal placées.

    '''
    c: int = 0
    indic: str = indice(mot_deviner, mot_propose)
    for x in indic : 
        if x == "M" :
            c += 1
    return c


def mastermind(mot_deviner: str) -> None :
    '''
    Procédure permetant de jouer au Mastermind simplifié :
        - Deviner un mot de 4 lettre composé obligatoirement de A,B,C,D, E ou F.
        - 10 tentative au maximum.
    
    '''
    tentative: int = int(input("Combien de tentative voulez-vous faire ? \n"))
    if tentative > 10 or tentative < 1 : 
         print("Erreur : le nombre de tentative doit être compris entre 1 et 10.")
         return
    
    i: int = 1
    while tentative != 0 :
        print(f"Tentative n°{i} : ")
        tmp: str = input()
        if not verifier(tmp) :
            print(f"{tmp} ne vérifie pas les onditions du MasterMind.")
            return
        if comparaison(mot_deviner, tmp) :
            print("Bravo !")
            return
        else :
            indice1: str = indice(mot_deviner, tmp)
            print(f"indice : {indice1} \n")
        i += 1
        tentative -= 1
    print("Perdu !") 
    return
    

def test() -> bool :
    
    assert nombre_mot("un deux et un") == 4, "Échec test 1 : nombre_mot()"
    assert nombre_mot("") == 0, "Échec test 2 : nombre_mot()"
    
    assert normalise("  HelLO WorLd ") == "helloworld" , "Échec test 3 : normalise()"
    assert comparaison("Test  ", "Te   st "), "Échec test 4 : comparaison()"
    assert not comparaison("Hello world", "Test"), "Échec test 5 : comparaison()"
    
    assert verifier("ABFD"), "Échec test 6 : verifier()"
    assert not verifier("AZFD"), "Échec test 7 : verifier()"
    assert not verifier("ABFDA"), "Échec test 8 : verifier()"
    
    assert lettre_appartient("a", "apprenti"), "Échec test 9 : lettre_appartient()"
    assert not lettre_appartient("a", "zpprenti"), "Échec test 10 : lettre_appartient()"
    assert not lettre_appartient("a", ""), "Échec test 11 : lettre_appartient()"
    
    return True
    

def main() :
    '''
    Procédure principale.

    '''
    if test() : 
        mastermind("ABEF")


main()

