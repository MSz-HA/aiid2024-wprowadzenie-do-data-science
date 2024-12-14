# Funkcjonalność, którą ma dostarczać moduł:
#  Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.
#  Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie.
#  Wypisanie danych datasetu – funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów
# wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma
# zostać wyświetlony (na wzór slice),
#  Podział datasetu na zbiór treningowy, testowy i walidacyjny. Funkcja przyjmuje 3 parametry określające
# procentowo jaka część głównego zbioru danych trafia do poszczególnych zbiorów.
#  Wypisz liczbę klas decyzyjnych – wypisanie krotek gdzie pierwsza wartość to wartość klasy (np. nazwa irysa,
# dla binarnych 0 lub 1 itd.), a druga to liczebność (kardynalność) tej klasy.
#  Wypisz dane dla podanej wartości klasy decyzyjnej – wypisuje wiersze z zadaną wartością klasy decyzyjnej.
#  Zapisanie danych do pliku csv – jako parametr przyjmowana jest dowolna lista, która może być podzbiorem
# datasetu, zmienną przechowującą dane treningowe, itp. Dodatkowo podawana jest nazwa pliku, do którego
# dane zostaną zapisane.
import csv

def wczytanie_datasetu(sciezka, czy_etykieta = False):
    global etykieta,lista
    etykieta = []
    lista = []

    try:
        with open(sciezka, mode='r', newline='', encoding='utf-8') as file:
            odczyt = csv.reader(file, delimiter=',')
            if czy_etykieta:
                etykieta = next(odczyt, [])
            lista = [wiersz for wiersz in odczyt]
    except FileNotFoundError:
        print(f"Błąd: Plik {sciezka} nie został znaleziony.")
    except Exception as e:
        print(f"Błąd: {e}")

def wypisanie_etykiet():
    if etykieta: print(etykieta)
    else: print('Nie było etykiet w danym datasecie')

def wypisanie_danych(poczatek = 0, koniec = None):
    if koniec is None:
        koniec = len(lista)
    print(lista[poczatek:koniec])

def podzial_datasetu(trening,test,walidacja):
    n = len(lista)
    trening = int(trening * n)
    test = int(test * n)
    walidacja = int(walidacja * n)

    return lista[:trening], lista[trening:trening + test], lista[trening + test:trening + test + walidacja]

def klasy_decyzyjne(numer_kolumny_klasy_decyzyjnej = 0):
    klasy = []

    for wiersz in lista:
        klasy.append(wiersz[numer_kolumny_klasy_decyzyjnej])

    klasy_set = list(set(klasy))
    krotki_klas = []

    for element in klasy_set:
        krotki_klas.append((element, klasy.count(element)))

    print(krotki_klas)

def wypisanie_danych_klasy (klasa, numer_kolumny_klasy_decyzyjnej = 0):
    lista_klasy = [wiersz for wiersz in lista if wiersz[numer_kolumny_klasy_decyzyjnej]==klasa]
    print(lista_klasy)

def zapis_danych_do_pliku (lista_do_zapisu, nazwa_pliku):
    try:
        with open(nazwa_pliku,'w', newline='') as csvfile:
            zapis = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            zapis.writerows(lista_do_zapisu)
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku: {e}")

# Przykładowe komendy dla zbioru https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

# wczytanie_datasetu('wdbc.data',False)
# wypisanie_etykiet()
# wypisanie_danych()
# trening, test, walidacja = podzial_datasetu(0.3,0.3,0.4)
# klasy_decyzyjne(1)
# wypisanie_danych_klasy('M',1)
# zapis_danych_do_pliku(trening,'zapis.csv')