# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:39:14 2021

@author: Lister Leonardo
"""
x=[25,28,11,23,1,65,7]

x.sort()
print(x)

b=['Curso', 'de', 'Python']
' '.join(b) #unir todos los elementos de la lista b 

c= '2;4;8;9;7;9;58'
c.split(';')

d=  '                    hdfg          '
d.strip()


#%% Ejemplo convertir los elementos de una lista str a entero

str_list=c.split(";")
str_list[1]

int(str_list[1])
int_list=[]

for i in str_list:
    int_list.append(int(i))
    


#%% Crear listas numericas implicitas dentro de la lista

c=list(range(5))

b=[i for i in range(5)]

e=[[i] for i in range(5)]

#nlista de numeros enteros aleatorios

from random import randint

g= [[randint(0,10)] for i in range(10)]


#Crear listas numericas de manera explicita for fuera de la lista
x=[]
for i in range(5):
    x.append(i)



#%%TUPLAS

mytyple=(1,2,3)


