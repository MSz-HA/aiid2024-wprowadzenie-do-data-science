# Wykorzystując listing 7 wypisz na konsoli 10 wybranych znaków niestandardowych (np. litery z alfabetu greckiego, symbole walut - (funt, bitcoin)) wypisując jednocześnie jego kod z tablicy unicode.

znaki_unicode = '§#«±🂣'

for znak in znaki_unicode:
    print(znak,' kod z tablicy unicode: ',znak.encode('utf-8'))