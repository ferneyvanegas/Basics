'''
Un vendedor recibe un sueldo base más un 10% extra porcomisión de sus ventas. 
El vendedor desea saber: 
    * Cuánto dinero obtendrá por concepto de comisiones por las ventas que realiza en el mes
    * El total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
'''
import os

try:
    base_salary = float(input('Ingrese el salario base\n>'))
    month_sales = int(input('Ingrese el valor total de las ventas hechas en el mes\n>'))
    commission = month_sales * .10
    os.system('clear')

    # Resultados
    print(f'\n| Siendo ${base_salary} tu salario base: |\n\n'
        f'>> La comisión por las ventas realizadas es de ${commission:,.2f} (10%)\n'
        f'>> El total que recibirás en dinero es: '
        f'${(base_salary + commission):,.2f} <<')
except ValueError as e:
    print(f'No es posible continuar. Se presentó el siguiente error:\n{e}')