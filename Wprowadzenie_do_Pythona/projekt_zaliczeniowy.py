# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.
import csv

with open('wdbc.data', mode='r', newline='', encoding='utf-8') as file:
    lista_1 = csv.reader(file, delimiter=' ', quotechar='|')
    for row in lista1:
        print(', '.join(row))
