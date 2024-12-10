# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.
import csv

def wczytanie_datasetu(sciezka,czy_etykieta):
    with open(sciezka, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        etykieta = []
        lista = []
        if czy_etykieta:
            etykieta = next(reader, None)

        for row in reader:
            lista.append(row)
            
        return(lista, etykieta)

lista, etykieta = wczytanie_datasetu('.\\Wprowadzenie_do_Pythona\\wdbc.data',0)
print(lista)
print(etykieta)