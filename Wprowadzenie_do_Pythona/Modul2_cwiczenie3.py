# Wyświetl na konsoli dowolny ciąg znaków i wykorzystaj wbudowane metody:
# title(),
# capitalize(),
# zfill(),
# upper(),
# count(),
# center().

ciag_znakow : str = input("Wprowadź dowolny ciąg znaków:\n")

print(ciag_znakow.title())
print(ciag_znakow.capitalize())
print(ciag_znakow.zfill(100))
print(ciag_znakow.upper())
print(ciag_znakow.count(" "))
print(ciag_znakow.center(100))