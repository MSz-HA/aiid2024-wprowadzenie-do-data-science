# Wykorzystując listing 7 wypisz na konsoli 10 wybranych znaków niestandardowych (np. litery z alfabetu greckiego, symbole walut - (funt, bitcoin)) wypisując jednocześnie jego kod z tablicy unicode.

# Zadanie 6
znaki_unicode = '§₿«±🂣'
print('znak', '\t', 'unicode')
for znak in znaki_unicode:
    print(znak,'\t', ord(znak))