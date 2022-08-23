text = input('Введите несколько слов через пробел: ')
g_char = ('a', 'e', 'i', 'o', 'u')

for word in text.split():
    if word.startswith(g_char):
        print(word + 'way', end=' ')
    else:
        new_word = word
        for char in word:
            if char not in g_char:
                new_word = new_word.lstrip(char) + char
            else:
                break
        print(new_word + 'ay', end=' ')

# Введите несколько слов через пробел: ioann zhanna yaroslav kirill igor archi
# ioannway annazhay aroslavyay irillkay igorway archiway 