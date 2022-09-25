from typing import Callable
from datetime import datetime
from random import randrange

CardHand = tuple[int, int, int, int, int]

# ИСПРАВИТЬ: функция декоратора возвращает вызываемый объект, не строку
def logger(func: Callable) -> Callable:
    """Выводит строку для журналирования выполнения функции, содержащую дату и время запуска функции, название функции, переданные аргументы и возвращаемое значение."""
    def _wrapper(*args, **kwargs):
        time_stamp = datetime.now()
        result = func(*args, **kwargs)
        # ИСПРАВИТЬ: служебная функция декоратора должна возвращать то же самое, что и декорируемая функция
        print(f"{time_stamp}:\t{func.__name__}:\t{args}:\t{kwargs}:\t{result}")
        return result
    return _wrapper           


@logger
# Подправил функцию checkhand: каре и фулл-хаус выдавали исключение: UnboundLocalError: local variable 'q' referenced before assignment, стрит возвращал None.
def checkhand(hand: CardHand) -> str:
    """Возвращает название самой старшей покерной комбинации в кортеже из пяти карт.

    Используются комбинации техасского холдема."""
    # ОТВЕТИТЬ: а что ещё можно сделать, чтобы получить уникальные карты?
    unique = set(hand)
    # unique = ()
    # for card in hand:
    #     if card not in unique:
    #         unique += (card,)
    lu = len(unique)
   
    if lu == 5:
        q = sorted(unique)
        if q == list(range(q[0], q[0]+5)):
            # КОММЕНТАРИЙ: да, это я пропустил, когда переписывал код в функцию — спасибо
            # edit by io25nsk
            # comb = 'стрит'
            return 'стрит'
        else:
            return 'старшая карта'
   
    if lu == 4:
        return 'пара'
    
    if lu == 3:
        # ИСПОЛЬЗОВАТЬ: учитывая, что мы используем все эти объекты только один раз:
        q = (hand.count(card) for card in unique)
        if max(q) == 2:
            return 'две пары'
        else:
            return 'сет'
    
    if lu == 2:
        # ИСПОЛЬЗОВАТЬ: учитывая, что мы используем все эти объекты только один раз:
        q = (hand.count(card) for card in unique)
        if max(q) == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    if lu == 1:
        return 'Шулер!'


# ИСПОЛЬЗОВАТЬ: может, лучше взять последний элемент, а не пятый?
result = ''
while result.split('\t')[-1] != 'сет':
    hand = ()
    for _ in range(5):
        hand += (randrange(1, 14),)
    result = checkhand(hand)
    # print(result)


# ИТОГ: очень хорошо — 5/7
