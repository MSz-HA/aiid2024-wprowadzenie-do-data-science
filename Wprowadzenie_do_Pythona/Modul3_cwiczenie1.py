#Zadanie 1
lista = list(range(1, 11))
nowaLista = lista[5:]
lista = lista[:5]
print(lista)
print(nowaLista)

#Zadanie 2
lista = lista + nowaLista
lista.insert(0, 0)
lista.sort(reverse=True)
print(lista)
