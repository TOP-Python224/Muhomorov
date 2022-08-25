text = input('Введите предложение: ')

puncts = '.,!?-;:\''
res = []

for word in text.split():
    res += [word.strip(puncts)]

print(res)

# stdout:
# Введите предложение: Contractions include: don't, isn't, and wouldn't. This some word with both apostrof's: 'Python'.
# ['Contractions', 'include', "don't", "isn't", 'and', "wouldn't", 'This', 'some', 'word', 'with', 'both', "apostrof's", 'Python']
