from random import *

lista = []
multiplos = []

num = int(input('Escolha um número para ser múltiplo: '))

for i in range(20):
    lista.append(randint(1, 50))

    if lista[i] % num:
        multiplos.append(lista[i])

print(f'Lista: {lista}')
print(f'Multiplos de {num}: {multiplos}')