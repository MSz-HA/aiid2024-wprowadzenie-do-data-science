#Zadanie 3
text = input("Podaj losowy ciąg znaków:\n")
text = set(text.lower())
text = list(text)
text.sort()
print(text)