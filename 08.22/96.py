decimal = '0123456789'
sign = '+-'

def is_digital(text: str) -> bool:
    """Функция принимает на вход строку, удаляет пробелы и определяет, можно ли это строку считать целым числом."""
    # ИСПРАВИТЬ: в условии сказано, что проигнорировать можно только ведущие и замыкающие пробелы — а те, которые внутри игнорировать не стоит
    clear_text = text.strip()
    if clear_text[:1] in (sign + decimal):
        cnt = 1
        for char in clear_text[1:]:
            if char in decimal:
                cnt += 1
            else:
                # ИСПРАВИТЬ: а разве не стоило бы прервать цикл и вернуть False по первому нахождению нецифрового символа?
                return False
    else:
        return False
    return cnt == len(clear_text)

if __name__ == '__main__':
    print(is_digital(input('Введите строку: ')))

# stdout:
# Введите строку: 12345
# True

# Введите строку:  12345 
# True

# Введите строку:  +12345
# True

# Введите строку:  123d45
# False

# Введите строку:  +12.34d5
# False


# ИТОГ: неплохо — 2/3
