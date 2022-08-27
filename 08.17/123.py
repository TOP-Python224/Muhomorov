# ОТВЕТИТЬ: есть же строковый метод title(), зачем вы вытащили эту древность на свет божий?
# Столкнулся с тем, что метод title() считает некоторые знаки препинания разделителями и приводит
# строку например abc!def к виду Abc!Def. Для избежания такого поведения документация рекомендует 
# использовать функцию capwords (https://docs.python.org/3/library/stdtypes.html#str.title).
# Но я переписал код в соответствии с Вашими замечаниями и необходимость в capsword отпала.

# text = 'Ioann Zhanna! yaroslav, Kirill? Igor. archi Anton? Stepan sergey, What the hell?! Morepuncts!!??!!??,.'
text = input('Введите несколько слов через пробел: ')
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
puncts = (',', '.', '?', '!')

for word in text.split(' '):
    if word.endswith(puncts):
            # ИСПРАВИТЬ: а если два знака препинания подряд будут? (см. stdout 2)
        cnt = 0
        for punct in puncts:
            cnt += word.count(punct) 
        word_begin = word[:-cnt]
        word_end = word[-cnt:]
    else:
        word_begin = word
        word_end = ''
    
    if word.startswith(vowels):
        new_word = word_begin + 'way'
    else:
        for char in word_begin:
            if char not in vowels:
                word_begin = word_begin.lstrip(char) + char.lower()
            else:
                break
        new_word = word_begin + 'ay'
        if word.istitle():
            new_word = new_word.title()
    print(new_word + word_end, end=' ')
        
         # ИСПРАВИТЬ: более корректным был бы код, в котором любым способом формируется новое слово, после чего отрабатывает блок кода по добавлению знаков препинания

# stdout:
# Ioannway Annazhay! aroslavyay, Irillkay? Igorway. archiway Antonway? Epanst ergeysay,

# stdout 2:
# Введите несколько слов через пробел: What the hell?!
# Atwh eth ell?hay!

# stdout3:
# Введите несколько слов через пробел: Ioann Zhanna! yaroslav, Kirill? Igor. archi Anton? Stepan sergey, What the hell?! Morepuncts!!??!!??,.
# Ioannway Annazhay! aroslavyay, Irillkay? Igorway. archiway Antonway? Epanstay ergeysay, Atwhay ethay ellhay?! Orepunctsmay!!??!!??,. 

# ИТОГ: не лучший, но рабочий вариант — 1.8/2.4
