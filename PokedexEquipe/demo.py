from re import M
import numpy as np
import matplotlib.pyplot as plt
from function import calculPerimetre, calculAire, showResult,  EcrireFichier, jeux , equation, equation2ndDegree


num1 = 20
num2 = 3
num3 = num1 + num2
num4 = num1 / num2
result = num3 + num4 - 11.111
print(num1)
print(num2)
print(num3)
print(num4)
print(result)

#Chaine de caractère
str = "Mou" + 3 * "ha" + "!"
print(str)
print(str[1])
print(str[-1])
print(str[0:3])

#listes
ma_liste = ['banane', 42 , [], "fraises", 1+2]
print(ma_liste)
ma_liste.append("pomme")
print(ma_liste)
ma_liste.remove(42)
print(ma_liste)
print(ma_liste[2])
ma_liste.insert(2, "orange")
ma_liste.pop()
print(ma_liste)
ma_liste.clear()
print(ma_liste)

#listes nom

liste_nom= ['Theo', 'Nath' , 'Axel']
print(liste_nom)
liste_nom.sort()
print(liste_nom)

#conditions
#largueur = int(input('largueur du rectangle : '))
#longueur = int(input('longueur du rectangle : '))
#calculAire(largueur, longueur)
#calculPerimetre(largueur, longueur)
#showResult(largueur, longueur)
#val = calculAire(largueur, longueur)
#text = "%s" % calculAire(largueur, longueur)
#text= "l'aire de ce rectangle est de "+text
#print(text)
#EcrireFichier(text)
#f = open("index.html","r")

#find_str= input("Entrer la chaine de caractère")

#line = f.readline()
#equation()
equation2ndDegree()




