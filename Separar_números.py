num_desejados = []

for número in range(1000, 9999):

    num1 = número // 100
    num2 = número % 100

    soma = num1 + num2

    if soma * soma == número:
        num_desejados.append(número)

print(num_desejados)