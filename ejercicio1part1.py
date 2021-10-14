# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:32:18 2021

@author: aquiles zurita
"""

#print se usa para desplegar un mensaje en la pantalla
print('Empezando a trabajar con Python')
print('Realizado por: "Aquiles Zurita"')
print('Consultando los tipos de valores:')
print('El tipo de dato de 875 es: ')
#con type() vamos a encontrar el tipo de dato de lo que esta entre parentecis
print(type(875))
print('El tipo de dato de 4.89 es:')
print(type(4.89))
print('El tipo de dato del texto: Now is better than never. es:')
print(type ('Now is better than never.'))
print('El tipo de dato de 1.32 es:')
print(type(1.32))
print('¿El valor 5 + 8i corresponde a un valor entero?')
#isinstance(a,b) se usa para validar si el valor a corresponde con el tipo b
print (isinstance(5+8j, int))
print('¿El valor 8.2 corresponde a un valor entero?')
print (isinstance(8.2, int))
print('¿El texto: Readability counts. corresponde a un string?')
print (isinstance('Readability counts.', str))
