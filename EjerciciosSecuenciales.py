# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:56:18 2021

@author: Usuario
"""
"""
1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
"""
presion = float ( input ('Digite el valor de la presion : '))
volumen = float (input('Digite el valor del volumen :'))
temperatura = float(input('Digite el valor de la temperatura : '))
masa = ( presion * volumen ) / ( 0.37 * ( temperatura + 460 ) )
print(f'El valor de la masa es de : {masa}' )


"""
2. Calcular el número de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la fórmula es:
Num. Pulsaciones = (200 – edad) /10.
"""
edad = int(input('Digite el valor de la edad : '))
pulsaciones = (200 - edad)/10
print('El numero de pulsaciones es de :', pulsaciones)

