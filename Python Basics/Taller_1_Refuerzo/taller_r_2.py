'''
Una tienda ofrece un descuento del 15% sobre el total de la compra.
El cliente desea saber cuánto deberá pagar finalmente por su compra.
* Nota: El algoritmo asume que se hacen 3 compras
'''
import os

try:
    pro_1 = float(input('Ingresa el valor del producto:\n”>'))
    pro_2 = float(input('Ingresa el valor del producto:\n”>'))
    pro_3 = float(input('Ingresa el valor del producto:\n”>'))

    sum = pro_1 + pro_2 + pro_3
    desc = sum * .15

    os.system('clear')
    print('----------------------------------------')
    print(f'Total: ${sum:,.2f}\n'
        f'Descuento: ${desc:,.2f}\n'
        '________________________________________\n'
        f'Total a pagar: ${(sum-desc):,.2f}')
    print('----------------------------------------')
except ValueError as e:
    print(f'No se puede continuar debido al siguiente error:\n{e}')
