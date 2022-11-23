from time import sleep
from typing import Callable


def repeat_call(func: Callable) -> Callable:
    """Повторно (с задержкой в 5 сек.) вызывает декорируемую функцию в случае ее завершения с исключением."""
    def _wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except:
                print('Функция завершена с исключением')
                sleep(5)
    return _wrapper


@repeat_call
def test_func(a: iter) -> int | float:
    """Возвращает сумму элементов принятого итерируемого объекта."""
    return sum(a)


print(test_func([1, 2, 3, 4]))
print(test_func(1))


# stdout:
# 10
# Функция завершена с исключением
# Функция завершена с исключением
# Функция завершена с исключением
# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\09.28\3.py", line 10, in _wrapper
#     return func(*args, **kwargs)
#   File "d:\Step\python\ДЗ\09.28\3.py", line 21, in test_func
#     return sum(a)
# TypeError: 'int' object is not iterable

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\09.28\3.py", line 24, in <module>
#     print(test_func(1))
#   File "d:\Step\python\ДЗ\09.28\3.py", line 13, in _wrapper
#     sleep(5)
# KeyboardInterrupt
