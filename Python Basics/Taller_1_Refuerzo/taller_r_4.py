'''
Un maestro desea saber:
    * Qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de estudiantes.
'''

import os

try:
    womem = int(input('Cuántas mujeres hay en el grupo?:\n”>'))
    men = int(input('Cuántos hombres hay en el grupo?:\n”>'))
    total_students = womem + men
    

    os.system('clear')
    print('PORCENTAJES')
    print('----------------------------------------')
    print(f' + Mujeres: {round((womem * 100)/total_students)}%')
    print(f' + Hombres: {round((men * 100)/total_students)}%')
    print('----------------------------------------')
except ValueError as e:
    print(f'No se puede continuar debido al siguiente error:\n{e}')