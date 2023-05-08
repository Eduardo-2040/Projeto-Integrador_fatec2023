número = int(input('Digite um número de três algarismos: '))

num1 = número // 100
num2 = número % 100

print(f'{num1} + {num2} = {num1 + num2}')