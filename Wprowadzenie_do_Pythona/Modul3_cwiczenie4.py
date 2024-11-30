#Zadanie 4
miesiace = {1: 'styczen', 2: 'luty', 3: 'marzec', 4: 'kwiecien', 5: 'maj', 6: 'czerwiec', 7: 'lipiec', 8: 'sierpien',
            9: 'wrzesien', 10: 'pazdziernik', 11: 'listopad', 12: 'grudzien'}

#Zadanie 5
miesiace_en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
               9: 'september', 10: 'october', 11: 'november', 12: 'december'}
months = {'pl': miesiace, 'en': miesiace_en}
print(months['pl'][4])
print(months['en'][4])

#Zadanie 6
text = 'Marianna'
text = set(text)
text = list(text)
print(dict.fromkeys(text, 1))
