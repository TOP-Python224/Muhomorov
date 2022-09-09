# ИСПРАВИТЬ: старайтесь не использовать такой способ импорта — так вы не контролируете импортируемые имена и сильно повышается вероятность конфликта имён
from random import randint, uniform
from typing import SupportsFloat

seq_lst, seq_tpl, seq_str = [], (), ''
result = {}

# ИСПОЛЬЗОВАТЬ: когда переменная цикла не используется в теле цикла, то её имя заменяется на символ подчёркивания _
for _ in range(randint(5, 10)):
    seq_lst.append(uniform(0.0, 100.0))
for _ in range(randint(5, 10)):
    seq_str += str(uniform(0.0, 100.0)) + ' '
# ИСПОЛЬЗОВАТЬ: конкатенацию кортежей никто не отменял
for _ in range(randint(5, 10)):
    seq_tpl += (uniform(0.0, 100.0),)


# ИСПОЛЬЗОВАТЬ: в ситуации, когда у нас заданы определённое количество типов, и нам необходимо их перечислить в аннотации, то для этого можно создать отдельную переменную:
NumSeqType = list[SupportsFloat] | tuple[SupportsFloat, ...] | str
# ИСПРАВИТЬ: несоответствие аннотации возвращаемого типа и типа возвращаемого значения
def average(seq: NumSeqType) -> dict[float] | None:
    """Функция принимает на вход один аргумент: список, кортеж или строку, содержащий только целые или вещественные числа. Функция возвращает словарь, содержащий отсортированные по возрастанию среднее арифметическое, геометрическое, квадратичное и гармоническое, рассчитанное для элементов аргумента."""
    arithmetic = quadratic = harmonic = 0
    geometric = 1

    # ИСПОЛЬЗОВАТЬ: встроенная функция isinstance() больше подходит для таких проверок
    if not isinstance(seq, (list, tuple, str)):
        # ИСПОЛЬЗОВАТЬ: здесь лучше выбросить исключение
        raise TypeError('сообщение об ошибке типа')

    # ОТВЕТИТЬ: а нужно ли здесь перехватывать исключения? в коде верхнего уровня вы нигде не проверяете возвращаемое значение на None => оно не используется => лучше выбросить исключение
    # Возврат None был предусмотрен условием задачи.
    try: 
        if type(seq) == str:
            tmp_seq = []
            for num in seq.rstrip().split(' '):
                tmp_seq.append(float(num))
            seq = tmp_seq
    # ИСПРАВИТЬ: всегда старайтесь уточнить тип перехватываемого исключения — иначе перехватите все исключения
    except ValueError:
        return None

    seqlen = len(seq)

    # ИСПОЛЬЗОВАТЬ: традиция и привычка предписывают нам использовать имена переменных i, j, k только для индексов
    for num in seq:
        # ИСПОЛЬЗОВАТЬ: встроенная функция isinstance() больше подходит для таких проверок
        if not isinstance(num, (int, float)):
            # ИСПОЛЬЗОВАТЬ: здесь лучше выбросить исключение
            raise TypeError('сообщение об ошибке типа')
        else:
            # КОММЕНТАРИЙ: а вот это хороший заход, за один цикл вычислить все последовательности — хвалю!
            arithmetic += num
            geometric *= num
            quadratic += num*num
            harmonic += 1/num

    result['arithmetic'] = arithmetic / seqlen
    result['geometric'] = pow(geometric, 1/seqlen)
    result['quadratic'] = pow(quadratic/seqlen, 1/2)
    result['harmonic'] = seqlen / harmonic

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result


# print(average((1.0, 2, 'f', 4, 5)))
# print(average({}))
# print(average('1 2 b 4 5'))

print(*(f'{num:.1f}' for num in seq_lst), sep='  ')
print(average(seq_lst), end='\n\n')

print(*(f'{num:.1f}' for num in seq_tpl), sep='  ')
print(average(seq_tpl), end='\n\n')

print(*(f'{float(num):.1f}' for num in seq_str.split()), sep='  ')
print(average(seq_str), end='\n\n')


# stdout:
# None
# None
# None
# {'garmonic': 22.0122751381488, 'geometric': 29.048864608273163, 'arithmetic': 38.700776850103814, 'quadratic': 48.441235417302124}
# {'garmonic': 23.676973286212267, 'geometric': 30.000913493344964, 'arithmetic': 35.21254849273601, 'quadratic': 38.83815111069476}
# {'garmonic': 37.57167199479728, 'geometric': 42.407965023141934, 'arithmetic': 47.73395996531975, 'quadratic': 52.951380157962774}


# ИТОГ: ничего критичного, но хватает моментов, на которые необходимо обратить внимание — 4/6
