lancuch_znakow : str = input('Wprowadź dowolny łańcuch znaków:\n')

print("Pierwsza połowa:\n",lancuch_znakow[:int(len(lancuch_znakow)/2)])

print("Druga połowa:\n",lancuch_znakow[int(len(lancuch_znakow)/2):])

print("Co drugi znak od końca łańcucha:\n",lancuch_znakow[-2::-2])