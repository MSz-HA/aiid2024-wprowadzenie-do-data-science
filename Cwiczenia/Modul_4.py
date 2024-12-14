def zadanie_3():
    text = input("Podaj trzy liczby podzielone spacjami:\n")
    lista_liczb = text.rsplit(' ')
    if (0 < int(lista_liczb[0]) <= 10) and (
            (int(lista_liczb[0]) > int(lista_liczb[1])) or (int(lista_liczb[1]) > int(lista_liczb[2]))):
        print('Warunki spełnione')
    else:
        print('Warunki nie są spełnione')

#zadanie_3()


def zadanie_4():
    for i in range(0,51,5):
        print(i)

#zadanie_4()


def zadanie_5():
    while True:
        text = input('Podaj liczby przedzielone spacjami. By wyjść z programu wpisz "quit":\n')
        if text == 'quit':
            break
        else:
            lista_liczb = text.rsplit(' ')
            for liczba in lista_liczb:
                print(str(int(liczba)**2)+" ")

#zadanie_5()


def zadanie_6():
    print('Podaj ciąg liczb przedzielonych enterami. By zakończyć działanie programu wpisz "stop":\n')
    lista_liczb = []
    while True:
        text = input()
        if text == 'stop':
            print(lista_liczb)
            break
        else:
            lista_liczb.append(int(text))

#zadanie_6()


def zadanie_7_for():
    liczba = input('Podaj liczbę wielocyfrową:\n')
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    print(f'Wynik: {suma}')

#zadanie_7_for()


def zadanie_7_while():
    liczba = input('Podaj liczbę wielocyfrową:\n')
    suma = 0
    liczba = list(liczba)
    while len(liczba):
        suma += int(liczba.pop())
    print(f'Wynik: {suma}')

# zadanie_7_while()

def zadanie_8():
    wysokosc = input('Podaj wysokość wieży:\n')
    if int(wysokosc) > 10:
        print('Masz wieżo Babel.')
    else:
        for i in range(1, int(wysokosc) + 1):
            print('A' * i)

# zadanie_8()


def zadanie_9():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


# zadanie_9()


def zadanie_10():
    wysokosc = input('Podaj wysokość diamentu od 3 do 9, wyłącznie nieparzyste:\n')
    wysokosc = int(wysokosc)
    lista = list(range(1, wysokosc + 1, 2)) + list(range(wysokosc - 2, 0, -2))
    for i in lista:
        print(str('o' * i).center(wysokosc))

# zadanie_10()