'''
Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de tres exámenes parciales.
'''

import os

try:
    grade_1 = float(input('Ingresa la nota del parcial No. 1:\n”>'))
    grade_2 = float(input('Ingresa la nota del parcial No. 2:\n”>'))
    grade_3 = float(input('Ingresa la nota del parcial No. 3:\n”>'))

    final_grade = round((grade_1 + grade_2 + grade_3)/3,1)

    os.system('clear')
    print('----------------------------------------')
    print(f'Nota Final: {final_grade}')
    print('----------------------------------------')
except ValueError as e:
    print(f'No se puede continuar debido al siguiente error:\n{e}')