def zadanie1():
    linia_danych: str = input('Wprowadź linię danych:\n')
    separator_zrodlowy: str = input('Wprowadź separator źródłowy:\n')
    separator_docelowy: str = input('Wprowadź separator docelowy:\n')
    print(separator_docelowy.join(linia_danych.split(separator_zrodlowy)))
    print(linia_danych.replace(separator_zrodlowy, separator_docelowy))

#zadanie1()


def zadanie2():
    lancuch_znakow = input('Wprowadź dowolny łańcuch znaków:\n')
    print("Pierwsza połowa:\n", lancuch_znakow[:len(lancuch_znakow) // 2])
    print("Druga połowa:\n", lancuch_znakow[len(lancuch_znakow) // 2:])
    print("Co drugi znak od końca łańcucha:\n", lancuch_znakow[::-2])

#zadanie2()


def zadanie3():
    ciag_znakow: str = input("Wprowadź dowolny ciąg znaków:\n")
    print(ciag_znakow.title())
    print(ciag_znakow.capitalize())
    print(ciag_znakow.zfill(100))
    print(ciag_znakow.upper())
    print(ciag_znakow.count(" "))
    print(ciag_znakow.center(100))

#zadanie3()


def zadanie4():
    wejscie = input("Wprowadź dowolny łańcuch znaków\n")
    print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}")
    print(f"Łańcuch {wejscie} isalpha: {wejscie.isalpha()}")
    print(f"Łańcuch {wejscie} isascii: {wejscie.isascii()}")
    print(f"Łańcuch {wejscie} isprintable: {wejscie.isprintable()}")
    print(f"Łańcuch {wejscie} istitle: {wejscie.istitle()}")
    print(f"Łańcuch {wejscie} isupper: {wejscie.isupper()}")

#zadanie4()


def zadanie5():
    # z https://pyformat.info/ NEW:
    print('{:>10}'.format('test'))
    print('{:_<10}'.format('test'))
    print('{:^10}'.format('test'))
    print('{:.5}'.format('xylophone'))
    print('{:10.5}'.format('xylophone'))
    # f-string:
    print(f'{'test':>10}')
    print(f'{'test':_<10}')
    print(f'{'test':^10}')
    print(f'{'xylophone':.5}')
    print(f'{'xylophone':10.5}')

#zadanie5()


def zadanie6():
    znaki_unicode = '§₿«±🂣'
    print('znak', '\t', 'unicode')
    for znak in znaki_unicode:
        print(znak, '\t', ord(znak))

#zadanie6()