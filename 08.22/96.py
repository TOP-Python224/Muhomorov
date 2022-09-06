decimal = '0123456789'
sign = '+-'

def isDigital(text: str) -> bool:
    """Функция принимает на вход строку, удаляет пробелы и определяет, можно ли это строку считать целым числом."""
    clear_text = ''
        
    for char in text:
        if char == ' ':
            continue
        else:
            clear_text += char
        
    if clear_text[:1] in (sign + decimal):
        cnt = 1
        for char in clear_text[1:]:
            if char in decimal:
                cnt += 1
            else:
                continue
    else:
        cnt = 0
        for char in clear_text:
            if char in decimal:
                cnt += 1
            else:
                continue

    return cnt == len(clear_text)


if __name__ == '__main__':
    print(isDigital(input('Введите строку: ')))


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