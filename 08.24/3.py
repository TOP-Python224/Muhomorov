import random

def remove_min_max(lst: list, # Параметры позиционно-ключевые, и так понятно для чего они, поэтому их можно использовать и так и так.
                   n: int,
                   *,
                   update_lst: bool) -> None | list | str: # Параметр строго ключевой, т.к. его название вместе со значением улучшают читаемость кода.
    """Функция удаляет n минимальных и n максимальных значений из списка чисел."""
    
    if len(lst) < n * 2:
        return "'n' too big!"
    
    if update_lst:
        for i in range(n):
            lst.remove(min(lst))
            lst.remove(max(lst))
        return None
    else:
        new_lst = lst.copy()
        for i in range(n):
            new_lst.remove(min(new_lst))
            new_lst.remove(max(new_lst))
        return new_lst

print(remove_min_max(random.sample(range(-100, 101), 10), 3, update_lst=True))
print(remove_min_max(random.sample(range(-100, 101), 15), 4, update_lst=False))
print(remove_min_max(random.sample(range(-100, 101), 10), n=6, update_lst=False))
print(remove_min_max(random.sample(range(-100, 101), 15), 4, False))

# stdout:
# None
# [11, 59, 40, 34, 63, 39, 7]
# 'n' too big!
# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\08.24\3.py", line 28, in <module>
#     print(remove_min_max(random.sample(range(-100, 101), 15), 4, False)) 
# TypeError: remove_min_max() takes 2 positional arguments but 3 were given
