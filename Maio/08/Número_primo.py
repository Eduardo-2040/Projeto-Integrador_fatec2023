z = 0

número = int(input('Digite um número: '))

for i in range(1, número + 1):
    if número % i == 0:
        z += 1
    
if z == 2:
    print('Primo')

else:
    print('Não é primo')