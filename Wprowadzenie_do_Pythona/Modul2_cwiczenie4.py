# Wprowadź z klawiatury dowolny łańcuch znaków i zapisz go do zmiennej. Następnie bazując na przykładzie poniżej zapisz również wyniki dla metod isalpha(), isascii(), isprintable(), istitle(), isupper(). wejscie = input() print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}").

wejscie = input("Wprowadź dowolny łańcuch znaków\n")

print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}")
print(f"Łańcuch {wejscie} isalpha: {wejscie.isalpha()}")
print(f"Łańcuch {wejscie} isascii: {wejscie.isascii()}")
print(f"Łańcuch {wejscie} isprintable: {wejscie.isprintable()}")
print(f"Łańcuch {wejscie} istitle: {wejscie.istitle()}")
print(f"Łańcuch {wejscie} isupper: {wejscie.isupper()}")