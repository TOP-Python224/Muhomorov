from typing import Callable
from time import perf_counter_ns, sleep

def func_timer(func: Callable) -> str:
    """Выводит время выполнения вложенной функции.
       func: вложенная функция."""    
    def _wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        func(*args, **kwargs)
        stop_time = perf_counter_ns()
        result = (stop_time - start_time) / 1_000_000_000
        return f"Время выполнения функции {result:.3f} секунд.\n"
    return _wrapper

@func_timer
def test_func(repeat: int = 10, 
              timeout: float = 0.5) -> str:
    """Выводит заданное количество чисел с заданным интервалом.
       repeat: количество чисел.
       timeout: интервал между выводом чисел в секундах."""
    for _ in range(repeat):
        print(_, end=' ')
        sleep(timeout)

print(test_func(repeat=15, timeout=0.1))
print(test_func(10, 0.5))

#stdout:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 Время выполнения функции 1.6914296 секунд.

# 0 1 2 3 4 5 6 7 8 9 Время выполнения функции 5.0507752 секунд.