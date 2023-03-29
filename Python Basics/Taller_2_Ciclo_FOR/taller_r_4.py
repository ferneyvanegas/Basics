'''
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

import os
    
try:
    num = int(input('Ingresa un número entero positivo mayor que cero\n>'))
    if num > 0:
        os.system('clear') # Limpiar pantalla
        print(f'NÚMEROS IMPARES:\n')
        for i in range(1, num + 1, 2):
            print(f'{i} >', end=' ')
    else:
        print('Error: El número ingresado no es correcto')
except ValueError as e:
    print(f'No se puede continuar con el programa por el siguiente error:\n{e}')