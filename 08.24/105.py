dig_to_char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
char_to_dig = {v: k for k, v in dig_to_char.items()}

def from_decimal(number: int, 
                *,
                out_system: int = 16) -> str :
    """Функция преобразует десятичное число number в число в системе исчисления out_system, по умолчанию в шестнадцатеричную."""
    quotient = number // out_system
    remainder = number % out_system
    result = str(remainder)
    while quotient > 0:
        quotient, remainder = quotient // out_system, quotient % out_system
        if remainder > 9:
            result = str(dig_to_char[remainder]) + result
        else:
            result = str(remainder) + result
    return result

def to_decimal(number: str,
              *,
              in_system: int = 16) -> int:
    """Функция преобразует число number в системе исчисления in_system (по умолчанию шестнадцатеричной) в десятичное число."""
    result = 0
    number_len = len(number)
    for b in range(number_len):
        if number[b].isalpha():
            result += (char_to_dig[number[b].title()]) * (in_system ** (number_len - 1))
        else:
            result += int(number[b]) * (in_system ** (number_len - 1))
        number_len -= 1
    return result

def from_any_to_any(number: str, in_system_main: int, out_system_main: int) -> str:
    """Функция преобразует число number в системе исчисления in_system_main в число в системе исчисления out_system_main."""
    return from_decimal((to_decimal(str(number), in_system=in_system_main)), out_system=out_system_main)

number = input('Введите число в исходной системе исчисления: ')
in_system_main = int(input('Введите исходную систему исчисления (2-16): '))
out_system_main = int(input('Введите целевую систему исчисления (2-16): '))
if (2 <= in_system_main <= 16) and (2 <= out_system_main <= 16):
    print(from_any_to_any(number, in_system_main, out_system_main))
else:
    print('Введено некорректное значение исходной или целевой системы исчисления!')

# stdout:
# Введите число в исходной системе исчисления: 10011010010
# Введите исходную систему исчисления (2-16): 2
# Введите целевую систему исчисления (2-16): 10
# 1234
# 
# Введите исходную систему исчисления (2-16): 16
# Введите целевую систему исчисления (2-16): 10
# 1234
# 
# Введите исходную систему исчисления (2-16): 8
# Введите целевую систему исчисления (2-16): 2
# 10011010010
# 
# Введите число в исходной системе исчисления: 1234
# Введите исходную систему исчисления (2-16): 6
# Введите целевую систему исчисления (2-16): 12
# 2110
