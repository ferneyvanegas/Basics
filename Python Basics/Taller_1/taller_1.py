'''
Programa básico de lectura de datos, almacenamiento en variables e impresión en pantalla
'''

# Definición de variables
id = input("Digite Identificación\n>")
name = input("Digite Nombre\n>")
last_name = input("Digite Apellido\n>")
address = input("Digite Dirección\n>")
phone = input("Digite Teléfono\n>")
age = int(input("Digite Edad\n>"))
marital_status = input("Digite Estado Civil\n>")
children = int(input("Digite número de hijos\n>"))
height = float(input("Digite Estatura\n>"))
hiring_date = input("Digite Fecha contratación\n>")
basic_salary = int(input("Digite Salario básico\n>"))
working_days = int(input("Digite Días laborados\n>"))

# Impresión de datos de Usuario
print('\n******************************************')
print('*          FICHA DE USUARIO              *')
print('******************************************')
print(f'*    ID: {id}\n'
      f'*    Nombre: {name} {last_name}\n'
      f'*    Dirección: {address}\n'
      f'*    Teléfono: {phone}\n'
      f'*    Edad: {age}\n'
      f'*    Estado civil: {marital_status}\n'
      f'*    # Hijos: {children}\n'
      f'*    Estatura: {height} cm\n'
      f'*    Fecha contratación: {hiring_date}\n'
      f'*    Sueldo básico: {basic_salary}\n'
      f'*    Días laborados: {working_days}')
print('******************************************')