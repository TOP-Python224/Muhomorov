from math import lcm
from fractions import Fraction


def make_axis(fractions: tuple[Fraction]) -> str:
    """Выводит отрезок ось с отметками полученных рациональных дробей в виде строки."""
    axis_lcm = lcm(*denoms)
    denoms_iter = denoms.copy()
    denoms_iter.append(axis_lcm + 1)
    line_cnt = 0
    axis_line = ''
    for i in range(axis_lcm):
        if i == axis_lcm / denoms_iter[line_cnt]:
            axis_line += '|—'
            line_cnt += 1
        else:
            axis_line += '—'
    return axis_line


def make_axis_text(axis_line: str) -> str:
    """Выводит подписи рациональных дробей на отметках полученного отрезка оси в виде строк."""
    line_cnt = 0
    di = 0
    top_line = bottom_line = ' ' * len(axis_line)
    for i in range(len(axis_line)):
        if axis_line[i] == '|':
            if line_cnt % 2 == 0:
                top_line = top_line[:i-1] + '1/' + str(denoms[di]) + top_line[i+1:-1]
            else:
                bottom_line = bottom_line[:i-1] + '1/' + str(denoms[di]) + bottom_line[i+1:-1]
            di += 1
            line_cnt += 1
    return top_line, bottom_line


def draw_axis(fractions: tuple[Fraction]) -> None:
    """Выводит отрезок оси с отметками и подписями полученных рациональных дробей."""
    axis_line = make_axis(fractions)
    top_line, bottom_line = make_axis_text(axis_line)
    print(f" {top_line} ")
    print(f"|{axis_line}|")
    print(f"0{bottom_line}1")


# fractions = (Fraction('1/2'), Fraction('1/3'), Fraction('1/4'))
# fractions = (Fraction('1/2'), Fraction('1/3'), Fraction('1/4'), Fraction('1/5'), Fraction('1/6'))
fractions = Fraction('1/2'),
denoms = list(sorted([f.denominator for f in fractions], reverse=True))
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
