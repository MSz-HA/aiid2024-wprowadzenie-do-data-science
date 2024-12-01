def zadanie1():
    A = [1 / x for x in range(1, 11)]
    B = [i for i in range(1, (2 ** 10) + 1) if (i % 2 == 0 or i == 1)]
    C = [x for x in B if x % 4 == 0]
    print(A)
    print(B)
    print(C)


#zadanie1()


def zadanie2():
    import random
    macierz = [[random.randint(1, 100) for i in range(4)] for j in range(4)]
    print(macierz)
    lista = [macierz[i][i] for i in range(4)]
    print(lista)


# zadanie2()

def zadanie3():
    produkt = {
        'szklanka': 'szt',
        'jajko': 'szt',
        'mąka': 'kg'
    }
    przefiltrowane = [key for key, value in produkt.items() if value == 'szt']
    print(przefiltrowane)


# zadanie3()