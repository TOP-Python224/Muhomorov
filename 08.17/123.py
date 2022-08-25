# ОТВЕТИТЬ: есть же строковый метод title(), зачем вы вытащили эту древность на свет божий?
from string import capwords as caps


text = 'Ioann Zhanna! yaroslav, Kirill? Igor. archi Anton? Stepan sergey,'
# text = input('Введите несколько слов через пробел: ')
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
puncts = (',', '.', '?', '!')


for word in text.split(' '):
    if word.startswith(vowels):
        if word.endswith(puncts):
            # ИСПРАВИТЬ: а если два знака препинания подряд будут? (см. stdout 2)
            print(word[:-1] + 'way' + word[-1], end=' ')
        else:
            print(word + 'way', end=' ')
    
    else:
        new_word = word
        for char in word:
            if char not in vowels:
                new_word = new_word.lstrip(char) + char.lower()
            else:
                break
        
        if word.istitle():
            new_word = caps(new_word)

        # ИСПРАВИТЬ: более корректным был бы код, в котором любым способом формируется новое слово, после чего отрабатывает блок кода по добавлению знаков препинания
        if word.endswith(puncts):
            new_word_part = new_word.partition(word[-1])
            new_word = new_word_part[0] + new_word_part[2] + 'ay' + new_word_part[1]
        
        print(new_word, end=' ')

# stdout:
# Ioannway Annazhay! aroslavyay, Irillkay? Igorway. archiway Antonway? Epanst ergeysay,

# stdout 2:
# Введите несколько слов через пробел: What the hell?!
# Atwh eth ell?hay!


# ИТОГ: не лучший, но рабочий вариант — 1.8/2.4
