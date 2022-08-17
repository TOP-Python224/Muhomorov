year = int(input('Введите год: '))

if not year % 4 and year % 100 or not year % 400:
    print('ДА')
else:
    print('НЕТ')

