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

etykieta =[]
lista = []

def wczytanie_datasetu(sciezka,czy_etykieta):
    with open(sciezka, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')

        if czy_etykieta:
            row_1 = next(reader, None)
            etykieta.append(row_1)

        for row in reader:
            lista.append(row)


def wypisanie_etykiet():
    if etykieta: print(etykieta)
    else: print('Nie było etykiet w danym datasecie')

def wypisanie_danych(poczatek = 0, koniec = len(lista)):
    print(lista[poczatek:koniec])

print(len(lista))
wczytanie_datasetu('.\\Wprowadzenie_do_Pythona\\wdbc.data',0)
# print(lista[0:len(lista)])
print(len(lista))
wypisanie_danych()