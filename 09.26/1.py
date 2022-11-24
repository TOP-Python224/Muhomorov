from math import lcm
from fractions import Fraction as frac


# ИСПРАВИТЬ: параметр fractions не используется
# ИСПОЛЬЗОВАТЬ здесь и далее: чтобы не путаться в глобальных и локальных переменных настоятельно рекомендую называть их по-разному
def make_axis(fraction_numbers: tuple[frac]) -> str:
    """Возвращает строку, содержащую символьное представление отрезка горизонтальной оси с отметками полученных рациональных дробей."""
    axis_lcm = lcm(*denominators)
    denoms_iter = denominators.copy()
    denoms_iter.append(axis_lcm + 1)
    # ИСПОЛЬЗОВАТЬ: j_mark — индекс отметки на оси
    j_mark = 0
    # ИСПОЛЬЗОВАТЬ: axis — строка, которую возвращает функция make_axis()
    axis = ''
    for i in range(axis_lcm):
        if i == axis_lcm / denoms_iter[j_mark]:
            axis += '|—'
            j_mark += 1
        else:
            axis += '—'
    return axis


def make_axis_labels(axis_line: str) -> tuple[str, str]:
    """Выводит подписи рациональных дробей на отметках полученного отрезка оси в виде строк."""
    line_cnt = 0
    # ИСПОЛЬЗОВАТЬ: j_label — индекс очередной подписи
    j_label = 0
    # ИСПОЛЬЗОВАТЬ: в axis_line – line у вас это отрезок, а в top_line – line у вас строка — это усложняет чтение кода
    top_labels = bottom_labels = ' ' * len(axis_line)
    for i in range(len(axis_line)):
        if axis_line[i] == '|':
            if line_cnt % 2 == 0:
                top_labels = top_labels[:i-1] + '1/' + str(denominators[j_label]) + top_labels[i+1:-1]
            else:
                bottom_labels = bottom_labels[:i-1] + '1/' + str(denominators[j_label]) + bottom_labels[i+1:-1]
            j_label += 1
            line_cnt += 1
    return top_labels, bottom_labels


def draw_axis(fraction_numbers: tuple[frac, ...]) -> None:
    """Выводит отрезок оси с отметками и подписями полученных рациональных дробей."""
    axis_line = make_axis(fraction_numbers)
    top_labels, bottom_labels = make_axis_labels(axis_line)
    print(f" {top_labels} ")
    print(f"|{axis_line}|")
    print(f"0{bottom_labels}1")


fractions = (frac('1/2'), frac('1/3'), frac('1/4'))
# fractions = (frac('1/2'), frac('1/3'), frac('1/4'), frac('1/5'), frac('1/6'))
# fractions = frac('1/2'),
denominators = list(sorted([f.denominator for f in fractions], reverse=True))
draw_axis(fractions)


# stdout:

#    1/4  1/2
# |———|—|——|——————|
# 0    1/3        1

#           1/6    1/4              1/2
# |——————————|——|———|—————|——————————|——————————————————————————————|
# 0            1/5       1/3                                        1

#  1/2
# |—|—|
# 0   1
