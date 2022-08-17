units = {0: '', 1: 'one ', 2: 'two ', 3: 'three ', 
        4: 'four ', 5: 'five ', 6: 'six ', 7: 'seven ', 
        8: 'eight ', 9: 'nine ', 10: 'ten', 11: 'eleven ',
        12: 'twelve ', 13: 'thirteen ', 14: 'fourteen ', 15: 'fifteen ',        
        16: 'sixteen ', 17: 'seventeen ', 18: 'eighteen ', 19: 'nineteen '}     

tens = {2: 'twenty ', 3: 'thirty ', 4: 'forty ', 5: 'fifty ',
        6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninety '}

number = int(input('Введите сумму от 0 до 999: '))

dig1 = number // 100
dig2 = number % 100 // 10
dig3 = number % 10
dig2dig3 = number % 100

phrase1 = (f'{units[dig1]}hundred ' if dig1 > 0 else f'{units[dig1]}')
phrase2 = (f'{units[dig2dig3]}' if 0 <= dig2dig3 < 20 else f'{tens[dig2]}{units[dig3]}')

print(phrase1, phrase2, sep='')

# Введите сумму от 0 до 999: 0

# Введите сумму от 0 до 999: 5
# five

# Введите сумму от 0 до 999: 14
# fourteen

# Введите сумму от 0 до 999: 100
# one hundred

# Введите сумму от 0 до 999: 107
# one hundred seven

# Введите сумму от 0 до 999: 115
# one hundred fifteen

# Введите сумму от 0 до 999: 179
# one hundred seventy nine

# Введите сумму от 0 до 999: 190
# one hundred ninety

# Введите сумму от 0 до 999: 777
# seven hundred seventy seven 
