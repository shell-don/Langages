#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author : Mathis Pigassou
Chapitre 18 d'Exos-1 :
L-Systèmes : inventé par un biologiste hongrois Aristid
Lindenmayer en 1968 on peut aussi tracer des approximations itérées de courbes fractales
grâce au module turtle.
'''

from turtle import Turtle, done


# Activité 1 : Dessiner un L-système simple où une lettre est remplacer par un motif.


def trace_lsysteme(mot: str, angle: int = 90, echelle: int = 1) -> None :
    '''
    Returns
    -------
    None
        Affiche le dessin correspondant aux lettres de mot. Par défaut langle est de 90 degrés, 
        et à chaque fois que l'on avance, c'est de 100×echelle.
    
    '''
    turtle = Turtle()  
    turtle.speed(10)   
    
    for i in mot:
        if i == 'A' or i == 'B':  
            turtle.forward(echelle * 100)
        elif i == 'g':        
            turtle.left(angle)
        elif i == 'd':           
            turtle.right(angle)

    done()


def remplacer_1(mot: str, lettre: str, motif: str) -> str :
    '''
    Returns
    -------
    str
        remplace une lettre par un motif dans un mot. Renvoie ce mot.
    
    '''
    return mot.replace(lettre, motif)


def iterer_lsysteme(depart: str, regle: tuple, k: int ) -> str :
    '''
    Returns
    -------
    str
        Calcule le k-ème itéré du L-système associé au mot initial depart selon la règle regle.
        Renvoie le mot itéré k fois.
    
    '''
    if k == 0 : return depart 
    lettre, motif = regle
    for i in range(k):
       depart =  remplacer_1(depart, lettre, motif)
    return depart


# Activité 2 : Dessiner un L-système où deux lettres sont remplacé par un certain motif.


def trace_lsysteme2(mot: str, angle: int = 90, echelle: int = 1)  -> None :
    '''
    Returns
    -------
    None
        Affiche le dessin correspondant aux lettres de mot, comportant 2 lettres, A et B. Par défaut langle est de 90 degrés, 
        et à chaque fois que l'on avance, c'est de 100×echelle. 
    
    '''
    turtle = Turtle()  
    turtle.hideturtle()
    turtle.speed(10000000)
    for i in mot:
        if i == 'A' or i == 'B':  
            turtle.forward(echelle * 100)
        elif i == 'g':        
            turtle.left(angle)
        elif i == 'd':           
            turtle.right(angle)
        elif i == 'a' :
            turtle.penup()
            turtle.forward(echelle * 100)
            turtle.pendown()
    done()


def remplacer_2(mot: str, lettre1:str, motif1: str, lettre2: str, motif2: str) -> str :
    '''
    Returns
    -------
    str
        remplace deux lettres par leurs motif dans un mot. Renvoie ce mot.
    
    '''
    nouveau_mot = ''
    for i in mot:
       if i == lettre1 : 
           nouveau_mot += motif1
       elif i == lettre2 :
          nouveau_mot += motif2
       else:
           nouveau_mot += i
    return nouveau_mot


def iterer_lsysteme_2(depart: str, regle1: tuple, regle2: tuple, k: int) -> str :
    '''
    Returns
    -------
    str
        Calcule le k-ème itéré du L-système associé au mot initial depart selon deux règles regle1 et regle2.
        Renvoie le mot itéré k fois. 
    
    '''
    if k == 0 : return depart
    lettre1, motif1 = regle1
    lettre2, motif2 = regle2
    for i in range(k) :
        depart = remplacer_2(depart, lettre1, motif1, lettre2, motif2)
    return depart


# Activité 3 : Cas général


def trace_lsysteme3(mot: str, angle: int = 90, echelle: int = 1) -> None :
    
    # Initialisation de la tortue
    turtle = Turtle()
    turtle.hideturtle()
    turtle.right(90)
    turtle.penup()
    turtle.forward(350)
    turtle.right(180)
    turtle.speed(0)
    stack = []

    for i in mot :
        if i == 'A' or i == 'B':  
            turtle.forward(echelle * 100)
        elif i == 'g':        
            turtle.left(angle)  
        elif i == 'd':           
            turtle.right(angle)  
        elif i == 'a':  
            turtle.penup()       
            turtle.forward(echelle * 100)
            turtle.pendown()
        elif i == '[':  
            # Mémorise la position et l'orientation (angle)
            stack.append((turtle.position(), turtle.heading()))
        elif i == ']':  
            # Restaure la position et l'orientation
            if stack :  
                pos, heading = stack.pop()
                turtle.penup()
                turtle.goto(pos)
                turtle.setheading(heading)
                turtle.pendown()
    done()


def remplacer(mot: str, remplacements: dict ) -> str :
    '''
    Returns
    -------
    str
        Une itération du mot dont les lettres ont été 
        remplacé suivant les règles du dictionnaire.

    '''
    for lettre, motif in remplacements.items():
        mot = mot.replace(lettre, motif)
    return mot


def iter_remplacer(mot: str, remplacements: dict, k: int) -> str :
    '''
    Returns
    -------
    str
        La k-ème itération du mot dont les lettres ont été 
        remplacé suivant les règles du dictionnaire (type str).

    '''
    for i in range(k) :
        mot = remplacer(mot, remplacements)
    return mot




# Exemple activité 1 :
#trace_lsysteme(iterer_lsysteme('A', ('A', 'AgAdAdAgA'), 2), angle=90, echelle=1)

# Exemple activité 2 :
# Triangle de Sierpinski
#trace_lsysteme(iterer_lsysteme_2('AdBdB', ('A','AdBgAgBdA'),('B','BB'),3),-120,1)
# Dragon
#trace_lsysteme(iterer_lsysteme_2('AX', ('X','XgYAg'), ('Y','dAXdY'), 3), 90,1)
# Gosper
#trace_lsysteme(iterer_lsysteme_2('A', ('A','AgBggBdAddAAdBg'), ('B','dAgBBggBgAddAdB'), 3),60,1)

# Exemple activité 3 :
#trace_lsysteme2(iterer_lsysteme_2('AdAdAdA', ('A','AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA'), ('a','aaaaaa'), 2),90,0.05)
# Arbre
#trace_lsysteme3(iterer_lsysteme_2('X', ('X','Ad[[X]gX]gA[gAX]dX'), ('A','AA'), 5),23,0.05)
#trace_lsysteme3(iterer_lsysteme('A', ('A','A[gA]A[dA][A]'), 5),26,0.05)
trace_lsysteme3(iterer_lsysteme('A', ('A','A[gA]A[dA]A'), 4),26,0.08)
#trace_lsysteme3(iterer_lsysteme_2('X', ('X','A[gX]A[dX]AX'), ('A','AA'), 5),25,0.05)


