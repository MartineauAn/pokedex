from doctest import REPORT_CDIFF
from re import M
import numpy as np
import matplotlib.pyplot as plt
import random
from sympy import symbols, solve
import math 

def calculPerimetre(largueur, longueur):
    return 2 * (largueur + longueur)

def calculAire(largueur, longueur):
    return largueur * longueur

def showResult(largueur, longueur):
    x_rect = [0, 0, largueur, largueur, 0] # abscisses des sommets
    y_rect = [0 , longueur, longueur, 0, 0] # ordonnees des sommets
    plt.plot(x_rect, y_rect,"r")
    plt.show()

def EcrireFichier(text):
    fichier = open("data.txt", "a")
    fichier.write(text)
    fichier.close()

def jeux():
    r1 = random.randint(0,50)
    response = int(input('choissez un nombre : '))
    while (response!=r1):
        if (response>r1) :
             print("plus petit") 
        else :
            print("plus grand")
        response = int(input('choissez un nombre : '))
    print("gagné")

def equation():
    response = input('choissez un nombre : ')
    sol = solve(response)
    print(sol)

def equation2ndDegree():
    
    x = int(input('valeur x : '))
    y = int(input('valeur y : '))
    z = int(input('valeur z : '))

    if x == 0: 
        print("Input correct quadratic equation") 
    else:

        discri = y * y - 4 * x * z 

        sqrtval = math.sqrt(abs(discri)) 
        if discri > 0: 
            print(" real and different roots ") 
            print((-y + sqrtval)/(2 * x)) 
            print((-y - sqrtval)/(2 * x)) 

        elif discri == 0: 

            print(" real and same roots") 
            print(-y / (2 * x)) 

        # when discriminant is less than 0

        else:

            print("Complex Roots") 
            print(- y / (2 * x), " + i", sqrtval) 
            print(- y / (2 * x), " - i", sqrtval) 


def morpion():
    print("_ _ _")
    print("_ _ _")
    print("_ _ _")
