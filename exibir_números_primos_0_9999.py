números_primos = []

for i in range(0,999):

    z = 0

    for x in range(1, i + 1):
        if i % x == 0:
            z += 1
        
    if z == 2:
        números_primos.append(i)

    z = 0

print(números_primos)