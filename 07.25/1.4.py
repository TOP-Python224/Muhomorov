rates = {('a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'): 1,
        ('d', 'g'): 2,
        ('b', 'c', 'm', 'p'): 3,
        ('f', 'h', 'v', 'w', 'y'): 4,
        ('k', ): 5,
        ('j', 'x'): 8,
        ('q', 'z'): 10}

rating = 0

word = input('Введите слово: ')
for chr in word:
    for key, value in rates.items():
        if chr in key:
            rating += value

print(f'За слово {word} игрок получает {rating} очков')
   
# Введите слово: cat
# За слово cat игрок получает 5 очков

# Введите слово: civilization
# За слово civilization игрок получает 26 очков