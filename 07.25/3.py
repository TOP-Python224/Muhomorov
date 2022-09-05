word1 = input('Введите 1-е слово: ')
word2 = input('Введите 2-е слово: ')

if list(word1).sort() == list(word2).sort():
    print(f'Слова {word1} и {word2} являются анаграммами')
else:
    print(f'Слова {word1} и {word2} НЕ являются анаграммами')