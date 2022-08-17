dct = {1: 'one', 2: 'two', 3: 'three', 
       4: 'one', 5: 'two', 6: 'six', 
       7: 'seven', 8: 'eight', 9: 'one'}

query = input('Введите искомое значение: ')
res = []

for key in dct:
    if dct.get(key) == query:
        res.append(key)

print(res)

# Введите искомое значение: one
# [1, 4, 9]

# Введите искомое значение: six
# [6]

# Введите искомое значение: ten
# []