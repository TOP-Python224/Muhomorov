from math import sqrt
from typing import Callable


# ИСПРАВИТЬ: имена функций, параметров, переменных и чего бы то ни было ещё должны быть значащими — что такое my_round, key?
# ИСПОЛЬЗОВАТЬ: для аннотации объекта функции мы используем Callable, не Iterable
def my_round(func: Callable,
            *args: int | float, 
            return_str: bool = True) -> str | float:
    # ИСПОЛЬЗОВАТЬ: есть разные стили оформления строки документации, но все они сходятся на том, что первая строка документации должна быть насколько возможно лаконичной и должна отвечать на вопрос "что делает?"
    """Возвращает округлённое до двух знаков дробной части значение в виде str или float объекта.

    :param func: объект функции, возвращающей число
    :param args: произвольное количество аргументов для func
    :param return_str: преобразует в str (True, по умолчанию) или float (False)
    :returns: преобразованное возвращаемое значение функции func
    """
    result = func(*args)
    # ИСПОЛЬЗОВАТЬ: форматирование с помощью f-строк позволяет делать математическое округление — f'{result:.2f}'
    # return str(round(result, 2)) if key else float(round(result, 2))
    return f'{result:.2f}' if return_str else float(f'{result:.2f}')


print(my_round(
    lambda k, x, b: k * x + b,
    10, 12, 5
))
print(my_round(
    lambda a, b, c, x: a * x**2 + b * x + c,
    10.1, 12.1, 6.6, 5.01
))
print(my_round(
    # ИСПОЛЬЗОВАТЬ: почему же не воспользовались импортированной функций квадратного корня? она здесь весьма кстати
    lambda a, b, c: sqrt((a + b + c)**3),
    10, 12, 18
))
print(my_round(
    lambda a, b, c: sqrt((a + b + c)**3),
    1, 2, 8,
    return_str=False
))
print(my_round(
    lambda a, b: (a * b) / (a + b),
    10, 12,
    return_str=False))

print(type(my_round(
    lambda a, b: (a * b) / (a + b),
    10, 12,
    return_str=False
)))
print(type(my_round(
    lambda a, b: (a * b) / (a + b),
    10, 12
)))


# stdout:
# 125
# 320.73
# 252.98
# 36.48
# 5.45
# <class 'float'>
# <class 'str'>


# ИТОГ: очень хорошо — 11/12
