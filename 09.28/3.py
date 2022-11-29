from time import sleep
from typing import Callable


def repeat_call(max_calls: int = 3,
                timeout: int = 1,
                interception_last: bool = True,) -> Callable:
    """Повторно, с заданной задержкой, заданное количество раз, вызывает декорируемую функцию в случае ее завершения с исключением.
    :param max_calls: количество вызовов функции,
    :param timeout: время между вызовами функции,
    :param interception_last: перехватывать/не перехватывать последнее исключение.
    """
    def _decorator(func: Callable):
        def _wrapper(*args, **kwargs):
            # ИСПОЛЬЗОВАТЬ: чем вам так условный цикл здесь дался, фиксированное же количество вызовов
            calls_cnt = 1
            while calls_cnt <= max_calls:
                try:
                    calls_cnt += 1
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    sleep(timeout)
                    if calls_cnt == max_calls and not interception_last:
                        return func(*args, **kwargs)
            # СДЕЛАТЬ: но раз так хочется большей универсальности — инициатива наказуема — пишите теперь здесь, вместо обычного, параметризуемый декоратор, в который передаётся максимальное количество вызовов (2 по умолчанию), таймаут между вызовами (1 секунда по умолчанию) и логический ключ "перехватывать/не перехватывать последнее исключение" (True по умолчанию)
        return _wrapper
    return _decorator


@repeat_call(max_calls=5, timeout=1, interception_last=False)
def test_func(a: iter) -> int | float:
    """Возвращает сумму элементов принятого итерируемого объекта."""
    return sum(a)


# print(test_func([1, 2, 3, 4]))
print(test_func(1))


# stdout:
# @repeat_call(max_calls=5, timeout=1)
# 'int' object is not iterable
# 'int' object is not iterable
# 'int' object is not iterable
# 'int' object is not iterable
# 'int' object is not iterable
# None

# @repeat_call(max_calls=5, timeout=1, interception_last=False)
# 'int' object is not iterable
# 'int' object is not iterable
# 'int' object is not iterable
# 'int' object is not iterable
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\09.28\3.py", line 17, in _wrapper
#     return func(*args, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\09.28\3.py", line 31, in test_func
#     return sum(a)
#            ^^^^^^
# TypeError: 'int' object is not iterable
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\09.28\3.py", line 35, in <module>
#     print(test_func(1))
#           ^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\09.28\3.py", line 22, in _wrapper
#     return func(*args, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\09.28\3.py", line 31, in test_func
#     return sum(a)
#            ^^^^^^
# TypeError: 'int' object is not iterable


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


# ИТОГ: ждём с нетерпением — 4/6
