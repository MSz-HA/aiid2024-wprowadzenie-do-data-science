# Przejdź na stronę https://pyformat.info/, a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem, wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady na postać z użyciem f-string.

#z https://pyformat.info/ NEW:

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