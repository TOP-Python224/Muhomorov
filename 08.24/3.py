from random import sample, randrange as rr, choice
from numbers import Real


def remove_min_max(
        # КОММЕНТАРИЙ: возможно, я бы выделил список в строго-позиционный параметр, но это не является критичным в этой ситуации — в остальном согласен
        # Параметры позиционно-ключевые, и так понятно для чего они, поэтому их можно использовать и так и так
        # ИСПОЛЬЗОВАТЬ: при аннотации контейнеров мы можем также указывать тип их содержимого — например, все вещественные числа
        lst: list[Real],
        n: int,
        *,
        # КОММЕНТАРИЙ: полностью согласен
        # Параметр строго ключевой, т.к. его название вместе со значением улучшают читаемость кода.
        update_lst: bool) -> None | list:
    """Функция удаляет n минимальных и n максимальных значений из списка чисел."""
    if len(lst) < 2*n:
        # ИСПОЛЬЗОВАТЬ: лучше выбросить исключение
        raise ValueError("'n' is larger than 'lst' length")
    
    if update_lst:
        # КОММЕНТАРИЙ: отличный подход
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


print(remove_min_max(
    sample(range(-100, 101), 10),
    3,
    update_lst=True
))
print(remove_min_max(sample(range(-100, 101), 15), 4, update_lst=False))
print(remove_min_max(sample(range(-100, 101), 10), n=6, update_lst=False))
print(remove_min_max(sample(range(-100, 101), 15), 4, False))

# ИСПОЛЬЗОВАТЬ: альтернативный вариант теста
# LIMIT = 4
# for _ in range(LIMIT):
#     num_data = sample(range(-100, 101), rr(15, 21))
#     print(num_data)
#     num_data_cleared = remove_min_max(num_data,
#                                       n=rr(3, 6),
#                                       update_lst=choice((True, False)))
#     print(num_data_cleared if num_data_cleared else num_data, end='\n\n')


# stdout:
# None
# [11, 59, 40, 34, 63, 39, 7]
# 'n' too big!
# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\08.24\3.py", line 28, in <module>
#     print(remove_min_max(random.sample(range(-100, 101), 15), 4, False)) 
# TypeError: remove_min_max() takes 2 positional arguments but 3 were given


# ИТОГ: отлично! — 6/6
