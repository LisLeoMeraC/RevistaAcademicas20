# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:02:03 2021

@author: Lister Leonardo
"""

#%%Ejercicio 1 utilizando IF

llantas= int(input("Cantidad de llantas: "))
pInicio=float(input("Precio: "))

if llantas>4:
    pInicio=pInicio*0.9
valor= pInicio*llantas
print("El precio unitario es: ",valor)

#%%Ejercicio 2 sobre el pago de un empleado por su trabajo

horas=int(input("Horas Trabajadas: "))
tarifa=float(input("Tarifa por hora: "))
descuento=float(input("Descuento: "))
if horas>40:
    p= ((horas*tarifa)-descuento) +(horas-40)*1.5  #pago a la semana
else:
    p=horas*tarifa-descuento

print("El pago es: ",p)

#%%Ejercicio 3 Calificacion
c1=float(input("Calificacion 1: "))
c2=float(input("Calificacion 2: "))
c3=float(input("Calificacion 3: "))
t=0 #--->Iniciar variable
if c1>=c3 and c2>=c3:
    t= c1 + c2
else:
    if c1>=c2 and c3>=c2:
        t= c1+c3 
    else:
        t=c2+c3
print("La calificacion final es: ", t)



#%% pago  RESTAURANTE
c= float(input("Total a pagar: "))
if c<50:
    print("pago en efectivo")
else: 
    if c>=50 and c<=100:
        print("pago electronico")
    else:
        if c>100 and c<=200:
            print("pago con tarjeta de debito")
        else:
                print("pago con tarjeta de credito")


#$$ uso del elif
c= float(input("Total a pagar: "))
if c<50:
    print("pago en efectivo")
elif c>=50 and c<=100:
    print("pago electronico")
elif c>100 and c<=200:
    print("pago con tarjeta de debito")
else:
    print("pago con tarjeta de credito")
    
#%% CICLO WHILE
import random as rm
x=0
while x!=3:
    x=rm.randint(1, 6)
    print (x)
print("fin")
    
#%% CICLO FOR

#CORRER DENTRRO DE UNA LISTA

for i in[1,2,3,4,5,6,7,9,7]:
    print ("hola")

#con el comando range
for i in range (10):
    print(i)
    
for i in range (0,10,2):
    print(i)
    
    
    