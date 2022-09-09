dig_to_char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
# КОММЕНТАРИЙ: отлично
char_to_dig = {v: k for k, v in dig_to_char.items()}


def from_decimal(number: int,
                 *,
                 out_system: int = 16) -> str:
    """Преобразует десятичное число number в число в системе счисления out_system (по умолчанию в шестнадцатеричную)."""
    # ИСПРАВИТЬ: лучше в такой ситуации перезаписывать переменную number, которую вы всё равно нигде далее не используете — так можно было бы написать более компактный и легко читаемый цикл
    quotient = number // out_system
    remainder = number % out_system
    result = str(remainder)
    while quotient > 0:
        # ИСПОЛЬЗОВАТЬ: а ещё есть встроенная функция divmod()
        quotient, remainder = quotient // out_system, quotient % out_system
        if remainder > 9:
            # ИСПРАВИТЬ: избыточное преобразование в строку, значения в словаре и так уже строки
            result = str(dig_to_char[remainder]) + result
        else:
            result = str(remainder) + result
    return result


def to_decimal(number: str,
               *,
               in_system: int = 16) -> int:
    """Преобразует число number в системе счисления in_system (по умолчанию шестнадцатеричной) в десятичное число."""
    result = 0
    number_len = len(number)
    # ИСПРАВИТЬ: для переменной индекса мы используем имя i
    # ИСПОЛЬЗОВАТЬ: встроенную функцию enumerate() вместе с функцией range() — выполните её отдельно, посмотрите, как она работает
    # for i, j in enumerate(range(number_len-1, -1, -1)):
    for b in range(number_len):
        # ДОБАВИТЬ: проверку, что цифра соответствует заявленной исходной системе счисления, и выброс исключения ValueError, если это не так

        # ИСПРАВИТЬ: разве нас устроит любая буква? (см. тест ниже)
        if number[b].isalpha():
            result += char_to_dig[number[b].title()] * in_system**(number_len - 1)
        else:
            result += int(number[b]) * in_system**(number_len - 1)
        number_len -= 1
    return result


def from_any_to_any(number: str,
                    in_system_main: int,
                    out_system_main: int) -> str:
    """Преобразует число number в системе счисления in_system_main в число в системе счисления out_system_main."""
    return from_decimal(
        # ИСПОЛЬЗОВАТЬ: не надо лишних скобок, их и так много в жизни разработчика =)
        to_decimal(
            str(number),
            in_system=in_system_main
        ),
        out_system=out_system_main
    )


number = input('Введите число в исходной системе счисления: ')
in_system_main = int(input('Введите исходную систему счисления (2-16): '))
out_system_main = int(input('Введите целевую систему счисления (2-16): '))
if 2 <= in_system_main <= 16 and 2 <= out_system_main <= 16:
    print(from_any_to_any(number, in_system_main, out_system_main))
else:
    # ИСПРАВИТЬ: лучше выбросить исключение ValueError
    print('Введено некорректное значение исходной или целевой системы счисления!')


# stdout:
# Введите число в исходной системе счисления: 1a9z56Я
# Введите исходную систему счисления (2-16): 11
# Введите целевую систему счисления (2-16): 2
# Traceback (most recent call last):
#   ...
# KeyError: 'Z'


# ИТОГ: весьма неплохо — 5/8
