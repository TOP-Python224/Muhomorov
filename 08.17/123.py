from string import capwords as caps


text = 'Ioann Zhanna! yaroslav, Kirill? Igor. archi Anton? Stepan sergey,'
# text = input('Введите несколько слов через пробел: ')
g_char = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
puncts = (',', '.', '?', '!')


for word in text.split(' '):
    if word.startswith(g_char):
        if word.endswith(puncts):
            print(word[:-1] + 'way' + word[-1], end=' ')
        else:
            print(word + 'way', end=' ')
    
    else:
        new_word = word
        for char in word:
            if char not in g_char:
                new_word = new_word.lstrip(char) + char.lower()
            else:
                break
        
        if word.istitle():
            new_word = caps(new_word)

        if word.endswith(puncts):
            new_word_part = new_word.partition(word[-1])
            new_word = new_word_part[0] + new_word_part[2] + 'ay' + new_word_part[1]
        
        print(new_word, end=' ')

# stdout:
# Ioannway Annazhay! aroslavyay, Irillkay? Igorway. archiway Antonway? Epanst ergeysay,