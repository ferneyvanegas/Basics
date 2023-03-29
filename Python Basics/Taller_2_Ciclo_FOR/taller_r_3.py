'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).
'''
import os
    
try:
    age = int(input('Ingresa su edad?\n>'))
    os.system('clear') # Limpiar pantalla
    print(f'AÑOS CUMPLIDOS:\n')
    for i in range(1, age + 1):
        print(f'{i} >', end=' ')
except ValueError as e:
    print(f'No se puede continuar con el programa por el siguiente error:\n{e}')