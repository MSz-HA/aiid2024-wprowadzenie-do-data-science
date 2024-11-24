# Użyj funkcji input() aby pobrać łańcuch znaków z klawiatury i z użyciem wycinków (slice) wykonaj:
# podziel łańcuch na dwie części, w miarę możliwości równe, ale jeżeli długość łańcucha jest nieparzysta, np. 11 znaków to pierwszy ma długość 5, a drugi 6. Wyświetl te łańcuchy w oknie konsoli.
# wyświetl łańcuch składający się z co drugiego znaku licząc od końca łańcucha

lancuch_znakow = input('Wprowadź dowolny łańcuch znaków:\n')

print("Pierwsza połowa:\n",lancuch_znakow[:int(len(lancuch_znakow)/2)])

print("Druga połowa:\n",lancuch_znakow[int(len(lancuch_znakow)/2):])

print("Co drugi znak od końca łańcucha:\n",lancuch_znakow[::-2])