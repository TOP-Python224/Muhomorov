from math import lcm
from fractions import Fraction as frac


def make_axis() -> str:
    """Возвращает строку, содержащую символьное представление отрезка горизонтальной оси с отметками полученных рациональных дробей."""
    axis_lcm = lcm(*[f.denominator for f in sorted_fractions])
    fractions_iter = sorted_fractions + [frac(1/axis_lcm+1)]
    j_mark = 0
    axis = ''
    for i in range(axis_lcm):
        if i == axis_lcm * fractions_iter[j_mark]:
            axis += '|—'
            j_mark += 1
        else:
            axis += '—'
    return axis


def make_axis_labels(axis_line: str) -> tuple[str, str, bool]:
    """Возвращает строки подписи рациональных дробей для отметок полученного отрезка оси и чётность количества."""
    j_label = 0
    top_labels = bottom_labels = ' ' * len(axis_line)

    for i in range(len(axis_line)):
        if axis_line[i] == '|':
            n = str(sorted_fractions[j_label].numerator)
            d = str(sorted_fractions[j_label].denominator)
            if j_label % 2 == 0:
                top_labels = top_labels[:i-len(n)] + n + '/' + d + top_labels[i+len(d):-1]
            else:
                bottom_labels = bottom_labels[:i-len(n)] + n + '/' + d + bottom_labels[i+len(d):-1]
            j_label += 1
    return top_labels, bottom_labels, bool(j_label % 2)


def draw_axis() -> None:
    """Выводит отрезок оси с отметками и подписями полученных рациональных дробей."""
    axis_line = make_axis()
    top_labels, bottom_labels, is_labels_odd = make_axis_labels(axis_line)
    top_last_label, bottom_last_label = ('1', ' ')[::(1,-1)[is_labels_odd]]
    print(f" {top_labels}{top_last_label}")
    print(f"|{axis_line}|")
    print(f"0{bottom_labels}{bottom_last_label}")


fractions = (frac('1/2'), frac('1/3'), frac('1/4'), frac('1/5'), frac('1/6'), frac('1/8'))
sorted_fractions = list(sorted(fractions))
draw_axis()


# stdout:
# fractions = (frac('41/100'), frac('3/10'), frac('1/2'))
#                               3/10                  1/2
# |——————————————————————————————|———————————|—————————|——————————————————————————————————————————————————|
# 0                                        41/100                                                         1

# fractions = (frac('1/2'), frac('1/3'), frac('1/4'), frac('1/5'), frac('1/6'), frac('1/8'))
#                1/8        1/5               1/3                                                                                1
# |———————————————|—————|————|——————|——————————|————————————————————|————————————————————————————————————————————————————————————|
# 0                    1/6         1/4                             1/2


# ИТОГ: хорошо — 7/8
