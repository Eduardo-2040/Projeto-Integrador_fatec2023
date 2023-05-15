import random

lista = []
impares = []
pares = 0
count_pares = 0

for i in range(20):
    num = random.randint(1,50)
    lista.append(num)
    if num % 2 == 0:
        pares += num
        count_pares += 1
    else:
        impares.append(num)

media_pares = pares / count_pares

print(f'lista: {lista}')
print(f'Média dos pares: {media_pares}')
print(f'Pares: {pares}')
print(f'Impares: {len(impares)}')