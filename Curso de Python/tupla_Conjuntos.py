# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:36:40 2021

@author: Lister Leonardo
"""

#TUPLAS

myTuple= (1,2,3) #puedo crear una tupla con o sin parentesis

#%%*******************CONJUNTOS******************

u={4,5,6,8,9,12} #creamos un conjunto

v={4,5,4,8,4,12} #el conjunto no tiene elementos repetidos, los elimina

u[1]  #no se son idexables

lista1=[1,2,3]
p= set(lista1)   #crear un conjunto por medio de lista

lista2=[1,2,3,2,2,4]
p1=set(lista2)

# operaciones con conjuntos

x=[7,8,6,4,9,8,45,12,36,42,10,9] #lista
y=[4,8,9,6,12,4,8,3,4,8,12,14]

a= set(x)
b=set(y)

#intersecion

c= a & b

#union
c= a|b

c= a - b

c= a^b

x=list(set(x))

#%% DICCIONARIO
persona= {'nombre': 'Lister', 'apellido': 'Mera'}

persona['nombre'] #buscar elemento

persona['nombre']='Leonardo' #cambiar

persona['edad']= 21

for item in persona.items():
    print(item)
persona.items()
persona.keys()
persona.values()



#%%

fluidos={'tipoFluido':['agua','alcohol','metano'],
         'pesoMolecular':[1,0.7,0.1],
         'ph':[7,4,3]}


fluido=input("Ingrese el tipo de fluido: ")
idx= fluidos['tipoFluido'].index(fluido)

peso= fluidos['pesoMolecular'][idex]









