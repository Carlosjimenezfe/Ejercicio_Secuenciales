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

"""
3. Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida.
"""
personaUna = float(input("Digite la cantidad que invirtio : $"))
personaDos = float(input("Digite la cantidad que invirtio : $"))
personaTres = float(input("Digite la cantidad que invirtio : $"))

total = personaUna + personaDos + personaTres
p1 = (personaUna / total)*100
p2 = (personaDos / total)*100
p3 = (personaTres / total)*100

print(f'EL porcentaje del primer inversor es de {p1} %')
print(f'EL porcentaje del primer inversor es de {p2} %')
print(f'EL porcentaje del primer inversor es de {p3} %')

"""
4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final.
"""
saldoInicial = float(input('Digite el saldo inicial : $'))
interes = float (saldoInicial * 0.015)
total = saldoInicial + interes
print(f'El saldo final es de: ${total} ')