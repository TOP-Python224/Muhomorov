email = input('Введите e-mail: ')

if '@' in email and '.' in email[email.find('@'):]:
    print('Верно')
else:
    print('Неверно')
    