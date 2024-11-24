# Napisz fragment kodu, który wczyta trzy zmienne ze standardowego wejścia (np. funkcja input()):
# linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
# separator źródłowy
# separator docelowy
# Następnie zaimplementuj z użyciem metod str.split() oraz str.join() podzielenie danych wejściowych pierwszym separatorem, połączenie i wypisanie danych połączonych drugim separatorem. Czy można to zrobić prościej wykorzystując inne wbudowane metody?

linia_danych : str = input('Wprowadź linię danych:\n')
separator_zrodlowy : str = input('Wprowadź separator źródłowy:\n')
separator_docelowy : str = input('Wprowadź separator docelowy:\n')

print(separator_docelowy.join(linia_danych.split(separator_zrodlowy)))