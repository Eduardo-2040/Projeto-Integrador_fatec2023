from random import *

vetor_A = []
vetor_B = []

for i in range(10):
    vetor_A.append(randint(1, 50))

print(vetor_A)
escolha = int(input('Deseja multiplica tal lista por que número? \n-> '))

for i in vetor_A:
    vetor_B.append(i * escolha)

print(f'Vetor A: {vetor_A}')
print(f'Vetor B: {vetor_B}')