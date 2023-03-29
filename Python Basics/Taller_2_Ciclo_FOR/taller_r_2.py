# Haz una tabla de multiplicar usando el ciclo FOR
import os
    
try:
    num = int(input('Qué tabla de multiplicar deseas revizar?\n>'))
    os.system('clear') # Limpiar pantalla
    print(f'TABLA DEL {num}\n')
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
except ValueError as e:
    print(f'No se puede continuar con el programa por el siguiente error:\n{e}')
