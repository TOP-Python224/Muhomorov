# КОММЕНТАРИЙ: по самой функции и её обвязке см. комментарии к задаче 5 задания 08.22
from numbers import Real
from random import *

seq_lst = []
tmp_seq = []
seq_tuple = ()
seq_str = ''
result = {}

for i in range(randint(5, 10)):
    seq_lst.append(uniform(0.0, 100.0))
for i in range(randint(5, 10)):
    seq_str += str(uniform(0.0, 100.0)) + ' '
for i in range(randint(5, 10)):
    tmp_seq.append(uniform(0.0, 100.0))
seq_tuple = tuple(tmp_seq)


# ИСПОЛЬЗОВАТЬ: если вы располагаете параметр seq на первой позиции, то согласно условию он должен иметь возможность принимать как числовой объект, так и итерируемый объект, содержащий числа — и мы должны это проверить в теле функции
# ИСПОЛЬЗОВАТЬ: а для параметра args мы можем сразу писать аннотацию типов аргументов
NumSeq = list[Real] | tuple[Real, ...] | str
# ИСПРАВИТЬ: несоответствие аннотации возвращаемого типа и типа возвращаемого значения
def average(seq: Real | NumSeq, *args: Real) -> float:
# ИСПОЛЬЗОВАТЬ: либо, мы могли бы написать совсем другую сигнатуру:
# def average(*args: Real, seq: NumSeq = None) -> dict[str, float]:
    """Функция принимает на вход один аргумент: список, кортеж , строку или произвольное количество объектов, содержащих только целые или вещественные числа. Функция возвращает словарь, содержащий отсортированные по возрастанию среднее арифметическое, геометрическое, квадратичное и гармоническое, рассчитанное для элементов аргумента."""
    arithmetic = quadratic = harmonic = 0
    geometric = 1

    if len(args) != 0:
        # ИСПРАВИТЬ: что если в seq был передан контейнер, а дальше числа? вы получите список со вложенным контейнером под индексом 0 и числа далее
        seq = [seq] + [d for d in args]

    # ИСПРАВИТЬ: эту проверку лучше сделать до того, как вы попытаетесь что-то сделать с seq как со списком
    # ИСПРАВИТЬ: встроенная функция isinstance() больше подходит для таких проверок
    if type(seq) not in (list, tuple, str):
        # ИСПРАВИТЬ: здесь лучше выбросить исключение
        return None
    
    try: 
        if type(seq) == str:
            tmp_seq = []
            for i in seq.rstrip().split(' '):
                tmp_seq.append(float(i))
            seq = tmp_seq
    except:
        return None

    seqlen = len(seq)

    for i in seq:
        if type(i) not in (int, float):
            return None
        else:
            arithmetic += i
            geometric *= i
            quadratic += i*i
            harmonic += 1/i

    result['arithmetic'] = arithmetic/seqlen
    result['geometric'] = pow(geometric, 1/seqlen)
    result['quadratic'] = pow(quadratic/seqlen, 1/2)
    result['harmonic'] = seqlen/harmonic

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result


print(average((1.0, 2, 'f', 4, 5)))
print(average({}))
print(average('1 2 b 4 5'))
print(average(seq_lst))
print(average(seq_tuple))
print(average(seq_str))
print(average([1, 2, 3, 4.23]))
# Если использовать строку из задания ('0 2 0.12 1'), то при расчете средней гармонической возникает деление на 0, т.к. в знаменателе формулы 1/а.
print(average('0.1 2 0.12 1'))
print(average(-1, 1.5, -2, 2.5))

# stdout
# None
# None
# None
# {'garmonic': 22.0122751381488, 'geometric': 29.048864608273163, 'arithmetic': 38.700776850103814, 'quadratic': 48.441235417302124}
# {'garmonic': 23.676973286212267, 'geometric': 30.000913493344964, 'arithmetic': 35.21254849273601, 'quadratic': 38.83815111069476}
# {'garmonic': 37.57167199479728, 'geometric': 42.407965023141934, 'arithmetic': 47.73395996531975, 'quadratic': 52.951380157962774}


# СДЕЛАТЬ: доработайте согласно комментариям функцию из задачи 5 задания 08.22, и только затем, используя её, отполируйте функцию в этой задаче


# ИТОГ: не идеальный, но хороший вариант — 4/5
