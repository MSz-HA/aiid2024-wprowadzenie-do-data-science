#Zadanie 7
import string


text = input('Podaj dowolny łańcuch znaków:\n')
text_set = set(text)
text_letters = text_set & set(string.ascii_lowercase)
text_digits = text_set & set(string.digits)
print(f"W zdaniu '{text}' występuje {len(text_letters)} znaków wspólnych ze zbiorem string.ascii_lowercase, co stanowi {len(text_letters)/len(string.ascii_lowercase):.2%} % tego zbioru.")
print(f"W zdaniu '{text}' występuje {len(text_digits)} znaków wspólnych ze zbiorem string.ascii_lowercase, co stanowi {len(text_digits)/len(string.digits):.2%} % tego zbioru.")
