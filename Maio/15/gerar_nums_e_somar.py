import random

lista = []
pares = []
impares = []

for i in range(10):
    num = random.randint(1,50)
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'lista: {lista}')
print(f'Pares: {len(pares)}')
print(f'Impares: {len(impares)}')