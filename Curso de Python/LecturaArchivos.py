# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:47:28 2021

@author: Lister Leonardo
"""

#MANEJOS DE ARCHIVOS 

file= open ('archivo.txt')
file.read()
file.close()

#%%
file= open ('LigaCampeon.txt', mode='w') #escribir desde la primer linea
file.write("Va a ser campeon en este año, ya verán")
file.close()

#%%
import os
print(os.getcwd())

#%%
with open('LigaCampeon.txt',mode='a') as file: #escribir desde la ultima linea
    file.write('\n Y tambien vamos hacer campeon de la supercopa de ecuador')

