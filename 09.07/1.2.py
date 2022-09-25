from itertools import permutations
letters_set = {'a', 'r', 't', 5}
letters = ''

# ИСПРАВИТЬ:
#  во-первых, в общем случае множество может содержать не только строки
#  во-вторых, если функции необходима индексируемая последовательность для своей работы, то преобразование стоит делать в теле самой функции, а не в коде верхнего уровня
# По 1-му замечанию сделал пребразование в str, однако наличие не только строк во множестве ломает работу sorted, ему нужны объекты одинакового типа, поэтому ему лучше передавать уже обработанную строку.
# Если же перенести преобразование в тело функциипо 2-му замечанию, то для использования с sorted такое преобразование придется делать дважды, поэтому предлагаю оставить его на верхнем уровне.
for c in letters_set:
    letters += str(c)

def all_perms(elements):
    # КОММЕНТАРИЙ: главное, чтобы вы поняли, как он работает
    # Алгоритм не мой (
    """Генерирует перестановки для переданного множества элементов."""
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]                


generator_perm = all_perms(letters)
print(*list(sorted(generator_perm)))

itertool_perm = sorted(permutations(letters))
print(*[''.join(permut) for permut in itertool_perm])

# stdout:
# airt aitr arit arti atir atri iart iatr irat irta itar itra rait rati riat rita rtai rtia tair tari tiar tira trai tria
# airt aitr arit arti atir atri iart iatr irat irta itar itra rait rati riat rita rtai rtia tair tari tiar tira trai tria


# ИТОГ: очень хорошо — 6/8
