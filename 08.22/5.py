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


def average(seq: int | float) -> float:
    """Функция принимает на вход один аргумент: список, кортеж или строку, содержащий только целые или вещественные числа. Функция возвращает словарь, содержащий отсортированные по возрастанию среднее арифметическое, геометрическое, квадратичное и гармоническое, рассчитанное для элементов аргумента."""
    arithmetic = quadratic = garmonic = 0
    geometric = 1

    if type(seq) not in (list, tuple, str):
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
            garmonic += 1/i

    result['arithmetic'] = arithmetic/seqlen
    result['geometric'] = pow(geometric, 1/seqlen)
    result['quadratic'] = pow(quadratic/seqlen, 1/2)
    result['garmonic'] = seqlen/garmonic

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result


print(average((1.0, 2, 'f', 4, 5)))
print(average({}))
print(average('1 2 b 4 5'))
print(average(seq_lst))
print(average(seq_tuple))
print(average(seq_str))


# stdout:
# None
# None
# None
# {'garmonic': 22.0122751381488, 'geometric': 29.048864608273163, 'arithmetic': 38.700776850103814, 'quadratic': 48.441235417302124}
# {'garmonic': 23.676973286212267, 'geometric': 30.000913493344964, 'arithmetic': 35.21254849273601, 'quadratic': 38.83815111069476}
# {'garmonic': 37.57167199479728, 'geometric': 42.407965023141934, 'arithmetic': 47.73395996531975, 'quadratic': 52.951380157962774}
