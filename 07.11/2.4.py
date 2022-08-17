char_1 = input('Введите 1-ю букву: ')
num_1 = int(input('Введите 1-е число: '))
char_2 = input('Введите 2-ю букву: ')
num_2 = int(input('Введите 2-е число: '))

if char_1 == 'a':
    char_1 = 1
elif char_1 == 'b':
    char_1 = 2
elif char_1 == 'c':
    char_1 = 3
elif char_1 == 'd':
    char_1 = 4
elif char_1 == 'e':
    char_1 = 5
elif char_1 == 'f':
    char_1 = 6 
elif char_1 == 'g':
    char_1 = 7
elif char_1 == 'h':
    char_1 = 8
 
if char_2 == 'a':
    char_2 = 1 
elif char_2 == 'b':
    char_2 = 2 
elif char_2 == 'c':
    char_2 = 3 
elif char_2 == 'd':
    char_2 = 4
elif char_2 == 'e':
    char_2 = 5
elif char_2 == 'f':
    char_2 = 6 
elif char_2 == 'g':
    char_2 = 7
elif char_2 == 'h':
    char_2 = 8

if ((char_1 == char_2 and abs(num_1 - num_2) == 1) or 
    (num_1 == num_2 and abs(char_1 - char_2) == 1) or 
    (abs(char_1 - char_2) == 1 and abs(num_1 - num_2) == 1)):
    print('ДА')
else:
    print('НЕТ')

     
