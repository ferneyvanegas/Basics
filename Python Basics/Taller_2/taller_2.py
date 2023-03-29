'''
Este algoritmo mejora el Taller_1 y agrega condicionales
'''
import os
from datetime import datetime # Para calculo de Fechas

try:
    # Datos para que el usuario ingrese
    # ===================================================
    id = input("Digite Identificación\n>")
    name = input("Digite Nombre\n>")
    last_name = input("Digite Apellido\n>")
    address = input("Digite Dirección\n>")
    phone = input("Digite Teléfono\n>")
    birth_date = datetime.strptime(input("Ingresa tu fecha de nacimiento (día/mes/año | Ej: 02/08/2000)\n>"), "%d/%m/%Y")
    marital_status = int(input("Digite Estado Civil (1) Soltero | (2) Casado | (3) Otro\n>"))
    marital_status_desc = 'Soltero'
    if marital_status == 2:
        marital_status_desc = 'Casado'
    children = int(input("Digite número de hijos\n>"))
    height = float(input("Digite Estatura\n>"))
    hiring_date = input("Digite Fecha contratación (día/mes/año | Ej: 02/08/2000)\n>")
    basic_salary = int(input("Digite Salario básico\n>"))
    # Datos para calcular
    # ===================================================
    age = datetime.now().year - birth_date.year - (datetime.now().month < birth_date.month or # Fecha de Nacimiento
                                                datetime.now().day < birth_date.day)
    working_days = (datetime.now() - datetime.strptime(hiring_date, "%d/%m/%Y")).days # Días trabajados
    if working_days < 1: # Se hace esto por si el usuario ingresa una fecha anterior que de números negativos
        working_days = 0 

    bonus_prep = 0
    take_a_stroll = False
    commission = '0%'
    food_bonus = False

    # Bono de Prepensión
    if age > 55:
        bonus_prep = basic_salary * .5

    # Paseo
    if marital_status == 2 and children > 0:
        take_a_stroll = True

    # Comisión
    if basic_salary >= 1000000 and basic_salary <= 1500000:
        commission = f'{(basic_salary * .2):,.2f} (2%)'
    elif basic_salary > 1500000 and basic_salary <= 2000000:
        commission = f'{(basic_salary * .5):,.2f} (5%)'

    # Bono Alimentación
    if working_days > 20 and basic_salary < 1000000:
        food_bonus = True

    # ===================================================

    os.system('clear') # Limpíando pantalla para mostrar resultados
    
    # Impresión de datos de Usuario
    print('\n******************************************')
    print('*          FICHA DE USUARIO              *')
    print('******************************************')
    print(f'*    ID: {id}\n'
        f'*    Nombre: {name} {last_name}\n'
        f'*    Dirección: {address}\n'
        f'*    Teléfono: {phone}\n'
        f'*    Edad: {age}\n'
        f'*    Estado civil: {marital_status_desc}\n'
        f'*    # Hijos: {children}\n'
        f'*    Estatura: {height} cm\n'
        f'*    Fecha contratación: {hiring_date}\n'
        f'*    Sueldo básico: ${basic_salary:,.2f}\n'
        f'*    Días laborados: {working_days}\n'
        f'______________________________________________\n'
        f'Bono de prepensión: ${bonus_prep:,.2f}\n'
        f'Comisión: ${commission}\n'
        f'______________________________________________\n'
        )
    
    if not take_a_stroll and not food_bonus:
        print('No hay beneficios adicionales.')
    else:
        print('Beneficios adicionales:')
    
    if take_a_stroll:
        print('* Paseo en Diciembre')
    if food_bonus:
        print('* Bono de alimentación')
    
    print('******************************************')
except ValueError as e:
    print(f'No se puede continuar con la ejecución del programa. Se presentó el siguiente error:\n'
          f'{e}')