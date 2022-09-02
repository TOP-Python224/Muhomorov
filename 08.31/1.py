from math import sqrt
from typing import Iterable

def my_func(func: Iterable, 
            *args: int | float, 
            key: bool = True) -> str | float:
    """Функция принимает объект функции, динамический список аргументов для переданной функции и логический ключ.
       В зависимости от значения логического ключа функция возвращает либо объект float (False) либо str (True, по-умолчанию).
       В обоих случаях значение округлено до двух знаков после запятой."""
    result = func(*args)
    return str(round(result, 2)) if key else float(round(result, 2))

print(my_func(lambda k, x, b: k * x + b, 10, 12, 5))
print(my_func(lambda a, b, c, x: a * x**2 + b * x + c, 10.1, 12.1, 6.6, 5.01))
print(my_func(lambda a, b, c: (((a + b + c) ** 3)) ** (1/2), 10, 12, 18))
print(my_func(lambda a, b, c: (((a + b + c) ** 3)) ** (1/2), 1, 2, 8, key=False))
print(my_func(lambda a, b: (a * b) / (a + b), 10, 12, key=False))
print(type(my_func(lambda a, b: (a * b) / (a + b), 10, 12, key=False)))
print(type(my_func(lambda a, b: (a * b) / (a + b), 10, 12)))

#stdout:
# 125
# 320.73
# 252.98
# 36.48
# 5.45
# <class 'float'>
# <class 'str'>
