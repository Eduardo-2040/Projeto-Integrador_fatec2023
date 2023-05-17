número = int(input('Digite um número: '))

if número == 0:
    print(f'{número}! = 1')

resultado = 1

for sequencia in range(número, 0, -1):
    resultado = resultado * sequencia

print(f'{número}! = {resultado}') 