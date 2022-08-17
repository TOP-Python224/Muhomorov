age = int(input('Введите возраст: '))

if age <= 13:
   print('детство')
elif 14 <= age <= 24:
   print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость') 

