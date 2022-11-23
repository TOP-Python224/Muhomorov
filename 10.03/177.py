rim_to_arab = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}



def from_rim_to_arab(rim_num: str) -> int:
    """Конвертирует полученное римское число в арабское число и выводит его."""
    arab_num = 0
    len_rim = len(rim_num)
    if len_rim == 0:
        return arab_num
    elif len_rim == 1:
        arab_num += rim_to_arab[rim_num]
        return arab_num
    else:
        first, second = rim_to_arab[rim_num[0]], rim_to_arab[rim_num[1]]
        if first < second:
            arab_num += second - first + from_rim_to_arab(rim_num[2:])
            return arab_num
        else:
            arab_num += first + from_rim_to_arab(rim_num[1:])
            return arab_num


rim_input = input('Введите римское число: ')
print(from_rim_to_arab(rim_input))


# stdout: 
# Введите римское число: XIX
# 19
# Введите римское число: XLIII
# 43
# Введите римское число: MCCXXXIV
# 1234
