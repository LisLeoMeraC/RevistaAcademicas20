# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:46:41 2021

@author: Lister Leonardo
"""

# EJERCICIO 1  
# Calcular el area de un trinagulo dado su base y altura
base=3
altura=5

area_Triangula= (base*altura)/2
print("El area es: ",area_Triangula)

#Ejercicio 2
# calcule el area de cualquier triangulo pidiendo valores por teclado

base= float(input("Escribir el valor de la base: "))
altura=float(input("Escribir el valor de la altura: "))
area_Triangula=(base * altura)/2
print("El area es: ",area_Triangula)


#%%Ejercicio 3
# hallar el area de un circulo
radio= float(input("Radio: "))
areaCirculo= 3.1416*radio**2
print("El area es: ",areaCirculo)

#%%
import math
radio= float(input("Radio: "))
areaCirculo= math.pi*radio**2
print("El area es: ",areaCirculo)




#%%

import math
a= float(input("A: "))
b=  float(input("B: "))
c=  float(input("C: "))

t= (a+b+c)/2
s= math.sqrt(t*(t-a)*(t-b)*(t-c))

print("T: ",t)
print("S: ",s)
#otra forma para imprimir utilizando un solo print
print("Semiperimetro= {:-3f}".format(t), "\nArea={:.3f}".format(s))

