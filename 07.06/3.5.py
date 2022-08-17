number = input('Введите 4-значное число: ')

print(f"Результат - {''.join(sorted(number, reverse=True))}")
# or
print(f'Результат - {number[::-1]}')




