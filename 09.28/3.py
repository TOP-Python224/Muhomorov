from typing import Callable
from time import sleep
from sys import stderr


def repeat_call(*,
                max_calls: int = 2,
                timeout: float = 1,
                raise_last_exception: bool = False,) -> Callable:
    """Повторно, с заданной задержкой, заданное количество раз, вызывает декорируемую функцию в случае ее завершения с исключением.
    :param max_calls: максимальное количество попыток вызвать функцию,
    :param timeout: время между вызовами,
    :param raise_last_exception: выбрасывать (True) или нет исключение, если все вызовы завершились неудачей.
    """
    def _decorator(func: Callable):
        def _wrapper(*args, **kwargs):
            for calls_cnt in range(max_calls):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # для сохранения объекта исключения за пределами локального пространства имён блока except
                    last_exception = e
                    print(f"{e.__class__.__name__}: {e!s}", file=stderr)
                    sleep(timeout)
            else:
                if raise_last_exception:
                    ending = 's' if max_calls != 1 else ''
                    raise Exception(f"{func.__name__} fails {max_calls} time{ending}") from last_exception
        return _wrapper
    return _decorator


@repeat_call(max_calls=5, timeout=0.5, raise_last_exception=True)
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


# ИТОГ: хорошо — 4/6
