#programa que determina si un numero es par
N=int(input("Ingresar el numero : ")) #ingresamos el numero

if N%2 == 0: # vemos que el residuo de N entre 2 es 0
    print('N es par') #Presentamos la informacion  
else: #En caso de que no se cumpla la proposicion
    print('N es impar') # Damos la informacion cuando no se cumple el condicional

print('nuevo cambio') #cambio

import matplotlib.pyplot as plt #importamos la libreria matplotlib