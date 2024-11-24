linia_danych : str = input('Wprowadź linię danych:\n')
separator_zrodlowy : str = input('Wprowadź separator źródłowy:\n')
separator_docelowy : str = input('Wprowadź separator docelowy:\n')

print(separator_docelowy.join(linia_danych.split(separator_zrodlowy)))