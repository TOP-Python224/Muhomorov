from math import lcm
from fractions import Fraction as frac


# ИСПРАВИТЬ: параметр fractions не используется
# ИСПОЛЬЗОВАТЬ здесь и далее: чтобы не путаться в глобальных и локальных переменных настоятельно рекомендую называть их по-разному
def make_axis() -> str:
    """Возвращает строку, содержащую символьное представление отрезка горизонтальной оси с отметками полученных рациональных дробей."""
    axis_lcm = lcm(*[f.denominator for f in sorted_fractions])
    fractions_iter = sorted_fractions + [frac(1/axis_lcm+1)]
    # ИСПОЛЬЗОВАТЬ: j_mark — индекс отметки на оси
    j_mark = 0
    # ИСПОЛЬЗОВАТЬ: axis — строка, которую возвращает функция make_axis()
    axis = ''
    for i in range(axis_lcm):
        # КОММЕНТАРИЙ: чтобы учесть числитель (см. комментарии ниже) можно здесь умножить на саму дробь
        if i == axis_lcm * fractions_iter[j_mark]:
            axis += '|—'
            j_mark += 1
        else:
            axis += '—'
    return axis


def make_axis_labels(axis_line: str) -> tuple[str, str, int]:
    """Выводит подписи рациональных дробей на отметках полученного отрезка оси в виде строк."""
    line_cnt = 0
    # ИСПОЛЬЗОВАТЬ: j_label — индекс очередной подписи
    j_label = 0
    # ИСПОЛЬЗОВАТЬ: в axis_line – line у вас это отрезок, а в top_line – line у вас строка — это усложняет чтение кода
    top_labels = bottom_labels = ' ' * len(axis_line)

    for i in range(len(axis_line)):
        if axis_line[i] == '|':
            if line_cnt % 2 == 0:
                # ИСПРАВИТЬ: не обязательно '1/' (см. комментарии ниже)
                # ИСПРАВИТЬ: если числитель и/или знаменатель двузначные или более, то необходимо это учесть в срезах, чтобы не было смещения следующих и граничных подписей (см. пример ниже)
                top_labels = top_labels[:i-len(str(sorted_fractions[j_label].numerator))] \
                             + str(sorted_fractions[j_label].numerator) \
                             + '/' \
                             + str(sorted_fractions[j_label].denominator) \
                             + top_labels[i+len(str(sorted_fractions[j_label].denominator)):-1]
            else:
                bottom_labels = bottom_labels[:i-len(str(sorted_fractions[j_label].numerator))] \
                                + str(sorted_fractions[j_label].numerator) \
                                + '/' \
                                + str(sorted_fractions[j_label].denominator) \
                                + bottom_labels[i+len(str(sorted_fractions[j_label].denominator)):-1]
            j_label += 1
            line_cnt += 1
    return top_labels, bottom_labels, line_cnt % 2


def draw_axis() -> None:
    """Выводит отрезок оси с отметками и подписями полученных рациональных дробей."""
    axis_line = make_axis()
    top_labels, bottom_labels, line_cnt = make_axis_labels(axis_line)
    # КОММЕНТАРИЙ: вот это хороший ход, озаботиться граничными символами на последнем этапе, а не в основных вычислениях
    # КОММЕНТАРИЙ: я бы правда ещё учёл чередование подписей относительно подписи '1' — всё также, для того, чтобы избежать потенциального наложения подписей
    top_labels = (f" {top_labels}1", f" {top_labels} ")
    bottom_labels = (f"0{bottom_labels}", f"0{bottom_labels}1")
    print(top_labels[line_cnt])
    print(f"|{axis_line}|")
    print(bottom_labels[line_cnt])


# fractions = (frac('1/2'), frac('1/3'), frac('1/4'))
fractions = (frac('1/2'), frac('1/3'), frac('1/4'), frac('1/5'), frac('1/6'), frac('1/8'))
# fractions = frac('1/2'),
# fractions = (frac('41/100'), frac('3/10'), frac('1/2'), frac('13/15'))
# fractions = (frac('41/100'), frac('3/10'), frac('1/2'))
# ИСПРАВИТЬ: похоже, примеры ввели вас в заблуждение — но в условии было сказано, что функция принимает любые дроби в диапазоне от 0 до 1, а не только от 0 до 1/2 с числителем равным 1 — например, 19/23 — это означает, что нас интересуют не только знаменатели, но и числители
# КОММЕНТАРИЙ: не уверен, кстати, что в таких обстоятельствах имеет смысл создавать отдельные последовательности с числителями и знаменателями — сортировка корректно работает и для Fraction объектов — впрочем, это уже вам решать
sorted_fractions = list(sorted(fractions))
draw_axis()


# stdout:
#fractions = (frac('41/100'), frac('3/10'), frac('1/2'))
#                               3/10                  1/2
# |——————————————————————————————|———————————|—————————|——————————————————————————————————————————————————|
# 0                                        41/100                                                         1


# fractions = (frac('1/2'), frac('1/3'), frac('1/4'), frac('1/5'), frac('1/6'), frac('1/8'))
#                1/8        1/5               1/3                                                                                1
# |———————————————|—————|————|——————|——————————|————————————————————|————————————————————————————————————————————————————————————|
# 0                    1/6         1/4                             1/2


#    1/4  1/2
# |———|—|——|——————|
# 0    1/3        1

#           1/6    1/4              1/2
# |——————————|——|———|—————|——————————|——————————————————————————————|
# 0            1/5       1/3                                        1

#  1/2
# |—|—|
# 0   1

#  1/100                                              1/2
# |—|—————————|————————————————————————————————————————|——————————————————————————————————————————————————|
# 0          1/10                                                                                          1
#                                                                                                        ^^^

# СДЕЛАТЬ: перепишите функции с учётом любых дробей из диапазона 0...1


# ИТОГ: в целом код хороший, ждём работу над ошибками — 4/8
