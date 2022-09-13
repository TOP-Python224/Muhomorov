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
    # Переработал эту чать, т.к. некоторые десятичные числа некорректно преобразовывались в шестнадцатиричные.
    # Например: 1111110111101 -> 102B352CF713, хотя правильно 102B352CF7D.
    number = dig_to_char.get(remainder, remainder)
    while quotient > 0:
        # ИСПОЛЬЗОВАТЬ: а ещё есть встроенная функция divmod()
        quotient, remainder = quotient // out_system, quotient % out_system
        # Заодно и здесь переработал для единообразия.
        number = dig_to_char.get(remainder, str(remainder)) + str(number)
    return number


def to_decimal(number: str,
               *,
               in_system: int = 16) -> int:
    """Преобразует число number в системе счисления in_system (по умолчанию шестнадцатеричной) в десятичное число."""
    result = 0
    number_len = len(number)
    # ИСПРАВИТЬ: для переменной индекса мы используем имя i
    # ИСПОЛЬЗОВАТЬ: встроенную функцию enumerate() вместе с функцией range() — выполните её отдельно, посмотрите, как она работает
    # for i, j in enumerate(range(number_len-1, -1, -1)):
    # for i, j in enumerate(range(number_len-1, -1, -1)):
    for i in range(number_len):
        # ДОБАВИТЬ: проверку, что цифра соответствует заявленной исходной системе счисления, и выброс исключения ValueError, если это не так
        # ИСПРАВИТЬ: разве нас устроит любая буква? (см. тест ниже)
        if number[i].title() in char_to_dig:
            if 0 <= char_to_dig[number[i].title()] < in_system:
                result += char_to_dig[number[i].title()] * in_system**(number_len - 1)
            else:
                raise ValueError('Символ не соответствует системе счисления!')
        elif number[i].isdecimal():
            if 0 <=  int(number[i]) < in_system:
                result += int(number[i]) * in_system**(number_len - 1)
            else:
                raise ValueError('Символ не соответствует системе счисления!')
        else:
            raise ValueError('Введен недопустимый символ')
        number_len -= 1
        # number_len = j
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
    raise ValueError('Введено некорректное значение исходной или целевой системы счисления!')
    
# stdout:
# Введите число в исходной системе счисления: 1a9z56Я
# Введите исходную систему счисления (2-16): 11
# Введите целевую систему счисления (2-16): 2
# Traceback (most recent call last):
#   ...
# KeyError: 'Z'

# stdout2:
# Введите число в исходной системе счисления: 1a9z56Я
# Введите исходную систему счисления (2-16): 11
# Введите целевую систему счисления (2-16): 2
# Traceback (most recent call last):
#   File "d:\Step\python\rep\Muhomorov\08.24\105.py", line 72, in <module>
#     print(from_any_to_any(number, in_system_main, out_system_main))
#   File "d:\Step\python\rep\Muhomorov\08.24\105.py", line 60, in from_any_to_any
#     to_decimal(
#   File "d:\Step\python\rep\Muhomorov\08.24\105.py", line 49, in to_decimal
#     raise ValueError('Введен недопустимый символ')
# ValueError: Введен недопустимый символ


# ИТОГ: весьма неплохо — 5/8
