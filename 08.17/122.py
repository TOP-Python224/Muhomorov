# ИСПОЛЬЗОВАТЬ: не забывайте приводить к одному регистру для последующих сравнений
text = input('Введите несколько слов через пробел: ').lower()
vowels = ('a', 'e', 'i', 'o', 'u')

for word in text.split():
    if word.startswith(vowels):
        print(word + 'way', end=' ')
    else:
        new_word = word
        for char in word:
            if char not in vowels:
                # ИСПРАВИТЬ: с этой строкой вы не облажались только потому, что в английском языке нет словарных слов, начинающихся с удвоенной одинаковой согласной — а в общем случае, если вам нужно срезать один символ, то срез и используйте
                # Вроде работает с удвоенными согласными в начале - stdout2
                # new_word = new_word.lstrip(char) + char
                new_word = new_word[1:] + char
            else:
                break
        print(new_word + 'ay', end=' ')

# stdout:
# Введите несколько слов через пробел: ioann zhanna yaroslav kirill igor archi
# ioannway annazhay aroslavyay irillkay igorway archiway

# stdout2
# Введите несколько слов через пробел: ioann zzhanna yaroslav kkirill igor archi
# ioannway annazzhay aroslavyay irillkkay igorway archiway 

# ИТОГ: верно — 2.1/2.4
