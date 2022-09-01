from typing import Callable, Iterable

nominals = {'E6': (10, 15, 22, 33, 47, 68),
            'E12': (10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82),
            'E24': (10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91),
            'E48': (100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 
                    249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 
                    619, 649, 681, 715, 750, 787, 825, 866, 909, 953),
            'E96': (100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 
                    158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 
                    249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 
                    392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 
                    619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976)
            }

result = {} 
diffs = {}

def om_to_precision(input_om: str) -> float:
    """Функция принимает на вход необходимое сопротивление в омах и выдает на выходе 2-значное 
    и 3-значное числа, необходимые для выборки ближайшего номинала из всех рядов."""
    if '.' in input_om:
        input_om_float = float(input_om)
        if input_om_float < 1:
            low = input_om_float * 100
        elif input_om_float < 10:
            low = input_om_float * 10
        else:
            low = float(input_om) * 10**(2 - (len((input_om.partition('.')[0]))))
    else:
        low = int(input_om) * 10**(2 - len(input_om))
    return low, low * 10
    
def mymap(function: Callable, iterator: Iterable) -> list:
    """Функция возвращает список, заполненный данными рассчитанными вложенной функцией. """
    ret = []
    for elem in iterator:
        ret.append(function(elem, param))
    return ret

def diffs_nom_prec(nom: int, prec: int | float) -> int | float:
    """Функция принимает на вход номинал и значение, рассчитанное из введенных пользователем данных, и вычисляет их разность."""
    return abs(nom - prec)

om = input('Введите необходимое сопротивление: ')
precision = om_to_precision(om)

for eia in nominals:
    if eia in ('E6', 'E12', 'E24'):
        param = precision[0]
        diffs[eia] = mymap(diffs_nom_prec, nominals[eia])
    else:
        param = precision[1]
        diffs[eia] = mymap(diffs_nom_prec, nominals[eia])

for eia in diffs:
    min_diff = min(diffs[eia])
    curr_index = diffs[eia].index(min_diff)
    if diffs[eia].count(min_diff) == 1:
        result[eia] = nominals[eia][curr_index]
    else:
        result[eia] = [nominals[eia][curr_index]]
        result[eia] += [nominals[eia][curr_index + 1]]
                
print(result)        
        




