def zadanie3():
    text = input("Podaj trzy liczby podzielone spacjami:\n")
    lista_liczb = text.rsplit(' ')
    if (0 < int(lista_liczb[0]) <= 10) and (
            (int(lista_liczb[0]) > int(lista_liczb[1])) or (int(lista_liczb[1]) > int(lista_liczb[2]))):
        print('Warunki spełnione')
    else:
        print('Warunki nie są spełnione')

#zadanie3()

def zadanie_4():
    zakres = range(51)
    for i in zakres:
        if i % 5 == 0:
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