#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:41:56 2025

Code issu de "Rapport du Travail Encadré de Recherche : Factorisation et Corps finis" 
    Louis Coumau, Axel Durbet, Fivos Reyre, Sid Ali Zitouni Terki
Publié le 15 mai 2020

Algoritme de Lenstra : factorisation sur courbes elliptiques (1985)

"""


import random
import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def xgcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def addPQ(P, Q, a, n):
    xp, yp = P
    xq, yq = Q
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    if xp == xq and yq == -yp:
        return (0, 0)
    if P == Q:
        var = (2 * yp) % n
        if gcd(var, n) != 1:
            return (-1, var)
        ivar = xgcd(var, n)[1] % n
        lam = ((3 * xp**2 + a) * ivar) % n
    else:
        var = (xq - xp) % n
        if gcd(var, n) != 1:
            return (-1, var)
        ivar = xgcd(var, n)[1] % n
        lam = ((yq - yp) * ivar) % n
    xr = (lam**2 - xp - xq) % n
    yr = (lam * (xp - xr) - yp) % n
    return (xr, yr)


def Lenstra_machine(n, B, e, c):
    a = random.randint(2, n - 1)
    xp = random.randint(2, n - 1)
    yp = random.randint(2, n - 1)
    b = (yp**2 - xp**3 - a * xp) % n
    g = gcd(4 * a**3 + 27 * b**2, n)
    if g == n:
        return Lenstra_machine(n, B, e, c + 1)
    if g != 1:
        return g, e, c
    xr, yr = xp, yp
    xnr, ynr = xp, yp
    for v in range(2, B):
        for i in range(1, v):
            xnr, ynr = addPQ((xr, yr), (xnr, ynr), a, n)
            e += 1
            if xnr == -1:
                return gcd(ynr, n), e, c
        xr, yr = xnr, ynr
    return Lenstra_machine(n, B, e, c + 1)


def Lenstra(n):
    if n % 2 == 0:
        return 2, 0, 0
    if n % 3 == 0:
        return 3, 0, 0
    B = int(math.exp((1 / 2) * math.sqrt(math.log(n)) * math.sqrt(math.log(math.log(n)))))
    return Lenstra_machine(n, B, 0, 0)


# Exemple de factorisation
#n = 68718821377  # 131071 * 524287
#factor, ops, calls = Lenstra(n)
#other_factor = n // factor
#print(f"Facteurs trouvés: {factor} et {other_factor}")
#print(f"Vérification: {factor} * {other_factor} = {factor*other_factor}")