from random import *

multiplos_5 = []
lista = []

for i in range(20):
    lista.append(randint(1, 50))

    if lista[i] % 5 == 0:
        multiplos_5.append(lista[i])

print(f'lista: {lista}')
print(f'Multiplos de 5: {multiplos_5}')