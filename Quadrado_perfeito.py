número = int(input('Número: '))

contador = 0
x = 0

for impar in range(1, número, 2):
    x += impar

    if x == número:
        contador += 1

if contador == 1:
    print(f'{número} é quadrado perfeito.')

else:
    print(f'{número} não é quadrado perfeito.')