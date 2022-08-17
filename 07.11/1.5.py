odd_rows = 'aceg'

char_1 = input('Введите 1-ю букву: ')
num_1 = int(input('Введите 1-е число: '))
char_2 = input('Введите 2-ю букву: ')
num_2 = int(input('Введите 2-е число: '))

cond_1 = ((not num_1 % 2 and char_1 not in odd_rows) or 
    (num_1 % 2 and char_1 in odd_rows))
cond_2 = ((not num_2 % 2 and char_2 not in odd_rows) or 
    (num_2 % 2 and char_2 in odd_rows))


if (cond_1 and cond_2) or (not cond_1 and not cond_2):
    print('ДА')
else:
    print('НЕТ')


