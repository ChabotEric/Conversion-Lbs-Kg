# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:53:36 2021

@author: chabote
"""

from os import system

# Fonction de conversion

def conversion(masseLbs):
    masseKg = masseLbs * 0.45359237
    return masseKg

# Interface utilisateur

print("Conversion de livres en Kg\n")

masseLbs = float(input("Quel et votre poids en livres: "))

print("\nVotre poids en Kg est: ", conversion(masseLbs))

#system("pause")
