# КОММЕНТАРИЙ: по самой функции и её обвязке см. комментарии к задаче 5 задания 08.22
from random import randint, uniform
from typing import SupportsFloat

seq_lst, tmp_seq, seq_tpl, seq_str = [], [], (), ''
result = {}

for _ in range(randint(5, 10)):
    seq_lst.append(uniform(0.0, 100.0))
for _ in range(randint(5, 10)):
    seq_str += str(uniform(0.0, 100.0)) + ' '
for _ in range(randint(5, 10)):
    tmp_seq.append(uniform(0.0, 100.0))
# seq_tpl = tuple(tmp_seq)
for _ in range(randint(5, 10)):
    seq_tpl += (uniform(0.0, 100.0),)

# ИСПОЛЬЗОВАТЬ: если вы располагаете параметр seq на первой позиции, то согласно условию он должен иметь возможность принимать как числовой объект, так и итерируемый объект, содержащий числа — и мы должны это проверить в теле функции
# ИСПОЛЬЗОВАТЬ: а для параметра args мы можем сразу писать аннотацию типов аргументов
NumSeqType = list[SupportsFloat] | tuple[SupportsFloat, ...] | str
# ИСПРАВИТЬ: несоответствие аннотации возвращаемого типа и типа возвращаемого значения
# def average(seq: NumSeqType, *args: int | float) -> dict[str, float] | None:
# def average(*args: int | float) -> dict[str, float] | None:
# ИСПОЛЬЗОВАТЬ: либо, мы могли бы написать совсем другую сигнатуру:
# Пытался дописать существующую функцию - ушел в дебри, запутался ( Переписал функцию заново - получилось более громоздко, но работает...
def average(*args: SupportsFloat, seq: NumSeqType = None) -> dict[str, float]:
    """Функция принимает на вход произвольное количество объектов, содержащих только целые или вещественные числа и/или  список, кортеж, или строку, содержащие только целые или вещественные числа. Функция возвращает словарь, содержащий отсортированные по возрастанию среднее арифметическое, геометрическое, квадратичное и гармоническое, рассчитанное для элементов аргумента."""
    arithmetic = quadratic = harmonic = 0
    geometric = 1
    args_seq = [] 
    # ИСПРАВИТЬ: эту проверку лучше сделать до того, как вы попытаетесь что-то сделать с seq как со списком
    # ИСПРАВИТЬ: встроенная функция isinstance() больше подходит для таких проверок
    if args:
        for i in args:
            if not isinstance(i, (int, float)):
                raise ValueError(f'Неверный тип данных - "{i}"!')
            else:
                args_seq = list(args)
    if seq:
        try: 
            if type(seq) == str:
                str_seq = []
                for i in seq.rstrip().split(' '):
                    str_seq.append(float(i))
                seq = str_seq
        except ValueError:
            raise ValueError(f'Неверный тип данных - "{i}"!')
        if type(seq) == tuple:
            seq = list(seq)
    else:
        seq = []

    seq += args_seq
    seqlen = len(seq)
    
    for i in seq:
        if isinstance(i, (int, float)):
            arithmetic += i
            geometric *= i
            quadratic += i*i
            harmonic += 1/i
        else:
            raise TypeError(f'Неверный тип данных - "{i}"!')

    result['arithmetic'] = arithmetic/seqlen
    result['geometric'] = pow(geometric, 1/seqlen)
    result['quadratic'] = pow(quadratic/seqlen, 1/2)
    result['harmonic'] = seqlen/harmonic

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result

    # ИСПРАВИТЬ: что если в seq был передан контейнер, а дальше числа? вы получите список со вложенным контейнером под индексом 0 и числа далее
       
# print(average((1.0, 2, 'f', 4, 5)))
print(average(10, 20.6, 30, seq=('1 2 4 5')))
print(average(seq=seq_lst))
print(average(seq=seq_tpl))
print(average(seq=seq_str))
print(average(seq=[1, 2, 3, 4.23]))
# Если использовать строку из задания ('0 2 0.12 1'), то при расчете средней гармонической возникает деление на 0, т.к. в знаменателе формулы 1/а.
print(average(seq='0.1 2 0.12 1'))
print(average(-1, 1.5, -2, 2.5))
print(average({}))

# stdout: 
# {'harmonic': 3.28349146110057, 'geometric': 5.8943442317405434, 'arithmetic': 10.37142857142857, 'quadratic': 14.493151091858133}
# {'harmonic': 17.360792036964238, 'geometric': 37.719658001204, 'arithmetic': 50.43512233394132, 'quadratic': 55.765765230669835}
# {'harmonic': 47.76707282637002, 'geometric': 49.327460869903234, 'arithmetic': 50.8315424502492, 'quadratic': 52.21161123990368}
# {'harmonic': 34.853919040942884, 'geometric': 45.25949621357899, 'arithmetic': 54.881918382273966, 'quadratic': 62.0038677141442}
# {'harmonic': 1.9326099371787548, 'geometric': 2.244517027586113, 'arithmetic': 2.5575, 'quadratic': 2.823689961734468}
# {'harmonic': 0.20168067226890754, 'geometric': 0.3935979342530861, 'arithmetic': 0.805, 'quadratic': 1.120758671614902}
# {'harmonic': -9.23076923076923, 'arithmetic': 0.25, 'geometric': 1.6548754598234365, 'quadratic': 1.8371173070873836}
# Traceback (most recent call last):
#   File "d:\Step\python\rep\Muhomorov\08.24\4_1.py", line 87, in <module>
#     print(average({}))
#   File "d:\Step\python\rep\Muhomorov\08.24\4_1.py", line 38, in average
#     raise ValueError(f'Неверный тип данных - "{i}"!')
# ValueError: Неверный тип данных - "{}"!

# СДЕЛАТЬ: доработайте согласно комментариям функцию из задачи 5 задания 08.22, и только затем, используя её, отполируйте функцию в этой задаче


# ИТОГ: не идеальный, но хороший вариант — 4/5
