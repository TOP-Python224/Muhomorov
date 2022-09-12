from typing import Callable
from datetime import datetime
from random import randrange

CardHand = tuple[int, int, int, int, int]

def logger(func: Callable) -> str:
    """Выводит строку для журналирования выполения функции, содержащую дату и время запуска функции, название функции, переданные аргументы и возвращаемое значение."""
    def _wrapper(*args, **kwargs):
        time_stamp = datetime.now()
        result = func(*args, **kwargs)
        return f"{time_stamp}:\t{func.__name__}:\t{args}:\t{kwargs}:\t{result}"
    return _wrapper           

@logger
# Подправил функцию checkhand: каре и фулл-хаус выдавали исключение: UnboundLocalError: local variable 'q' referenced before assignment, стрит возвращал None.
def checkhand(hand: CardHand, test=0) -> str:
    """Возвращает название самой старшей покерной комбинации в кортеже из пяти карт.
    Используются комбинации техасского холдема."""
    unique = ()
    for card in hand:
        if card not in unique:
            unique += (card,)
    lu = len(unique)
   
    if lu == 5:
        q = sorted(unique)
        if q == list(range(q[0], q[0]+5)):
            # edit by io25nsk
            # comb = 'стрит'
            return 'стрит'
        else:
            return 'старшая карта'
   
    if lu == 4:
        return 'пара'
    
    if lu == 3:
        q = ()
        for card in unique:
            q += (hand.count(card),)
        if max(q) == 2:
            return 'две пары'
        else:
            return 'сет'
    
    if lu == 2:
        # add by io25nsk
        q = ()
        for card in unique:
            q += (hand.count(card),)
        if max(q) == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    if lu == 1:
        return 'Шулер!'

result = '\t\t\t\t'
while result.split('\t')[4] != 'сет':
    hand = ()
    for _ in range(5):
        hand += (randrange(1, 14),)
    result = checkhand(hand)
    print(result)



    
   