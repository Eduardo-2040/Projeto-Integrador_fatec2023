from random import *

lista = []
pares = []
impares = []

for i in range(10):
    lista.append(randint(1, 50))
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    elif lista[i] % 2 != 0:
        impares.append(lista[i])

print(f'lista: {lista}')
print(f'Pares: {len(pares)}')
print(f'Impares: {len(impares)}')