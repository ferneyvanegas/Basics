'''
Encuentra la suma de todos los números pares del 1 al 100
'''
sum = 0
for i in range(0, 100 + 1, 2):
    sum+=i
print(f'La suma de todos los números pares del 1 al 100 es {sum}')