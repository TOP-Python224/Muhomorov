number = input('Введите любое целое число: ')
result = ''

for c in number:
    if not (c == '3' or c == '6'):
        result += c

print(result)

