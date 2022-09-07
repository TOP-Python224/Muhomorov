input_str = input('Введите двоичное число: ')
binary_set = {'0', '1'}
if input_str[:2].count('b') == 1:
    input_str = input_str.replace('b', '')
print('ДА') if set(input_str) == binary_set else print('НЕТ')

#stdout:
# Введите двоичное число: 0100101
# ДА

# Введите двоичное число: b0110
# ДА

# Введите двоичное число: 0b01001110
# ДА

# Введите двоичное число: 00b1001110
# НЕТ

# Введите двоичное число: 0b010071110
# НЕТ
