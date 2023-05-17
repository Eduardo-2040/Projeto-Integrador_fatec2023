from random import *

lista = []

escolha = int(input('Disponibilizar na ordem normal = 1 \nDisponibilizar na ordem inversa = 2 \n-> '))

for i in range(10):
    lista.append(randint(1, 50))

print(f'Lista normal: {lista}')

if escolha == 1:
    print(f'Sua lista: {lista}')

elif escolha == 2:
    #lista.reverse()
    #print(f'Sua lista: {lista}')

    for i in range(9, -1, -1):
        print(lista[i], end=' ')