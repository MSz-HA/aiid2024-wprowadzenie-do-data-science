def zadanie1():
    global lista, nowaLista
    lista = list(range(1, 11))
    nowaLista = lista[5:]
    lista = lista[:5]
    print(lista)
    print(nowaLista)

#zadanie1()


def zadanie2():
    global lista
    lista = lista + nowaLista
    lista.insert(0, 0)
    lista.sort(reverse=True)
    print(lista)

#zadanie2()


def zadanie3():
    text = input("Podaj losowy ciąg znaków:\n")
    text = set(text.lower())
    text = list(text)
    text.sort()
    print(text)

#zadanie3()


def zadanie4():
    global miesiace
    miesiace = {1: 'styczen', 2: 'luty', 3: 'marzec', 4: 'kwiecien', 5: 'maj', 6: 'czerwiec', 7: 'lipiec',
                8: 'sierpien', 9: 'wrzesien', 10: 'pazdziernik', 11: 'listopad', 12: 'grudzien'}

#zadanie4()


def zadanie5():
    miesiace_en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
                   9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    months = {'pl': miesiace, 'en': miesiace_en}
    print(months['pl'][4])
    print(months['en'][4])

#zadanie5()


def zadanie6():
    text = 'Marianna'
    print(dict.fromkeys(text, 1))

#zadanie6()


def zadanie7():
    import string
    text = input('Podaj dowolny łańcuch znaków:\n')
    text_letters = set(text.lower()) & set(string.ascii_lowercase)
    text_digits = set(text.lower()) & set(string.digits)
    print(
        f"W zdaniu '{text}' występuje {len(text_letters)} znaków wspólnych ze zbiorem string.ascii_lowercase, co stanowi {len(text_letters) / len(string.ascii_lowercase):.2%} tego zbioru.")
    print(
        f"W zdaniu '{text}' występuje {len(text_digits)} znaków wspólnych ze zbiorem string.ascii_lowercase, co stanowi {len(text_digits) / len(string.digits):.2%} tego zbioru.")

#zadanie7()


def zadanie8():
    text = input("Podaj trzy liczby całkowite podzielone spacjami:\n")
    lista_liczb = text.rsplit(' ')
    start = int(lista_liczb[0])
    stop = int(lista_liczb[1])
    step = int(lista_liczb[2])
    for i in range(start, stop, step):
        print(i)

#zadanie8()