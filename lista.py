def lista_while():

    L = [1, 2, 3, 4, 5]

    x = 0

    while x < len(L):
        print(L[x], end=' ')
        x += 1

def lista_for():

    L = [1, 2, 3, 4, 5]

    for item in L:
        print(item, end=' ')
    
def lista_adicionar_valor():

    L = [0] * 10

    print(L)

    for i in range(10):

        L[i] = int(input(f'{i + 1}° valor -> '))
        
        print(L)

def lista_append():

    L = [0] * 10

    print(L)

    for i in range(10):

        valor = int(input(f'{i + 1}° valor -> '))
        
        L.append(valor)
    
    print(L)

def lista_insert():

    L = []

    print(L)

    for i in range(10):

        L.insert(i, int(input(f'{i + 1}° valor -> ')))

        print(L)