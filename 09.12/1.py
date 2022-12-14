# ИСПОЛЬЗОВАТЬ: строковые литералы окружаются скобками только в том случае, если нам необходимо перенести литерал на другую строку в коде
br_open, br_close = '([{', ')]}'
br_trans = str.maketrans(br_close, br_open)

def check_lisp_line(line: str) -> bool:
    """Проверяет корректность синтаксиса переданной строки кода на языке LISP и возвращает True, либо False."""
    br_tmp = []
    for char in line:
        if char in br_open:
            br_tmp.append(char)
        if char in br_close:
            if not br_tmp:
                return False
            br_pair = char.translate(br_trans)
            if br_pair == br_tmp[-1]:
                # ОТВЕТИТЬ: сами придумали стек использовать или нашли?
                # Безрезультатно думал 2 дня, потом нашел про стек - все гениальное просто(
                br_tmp = br_tmp[:-1]
            else:
                return False
    return True if not br_tmp else False


print(check_lisp_line('(for-loop {[i 0 (< i 10) (inc i)]} (println i))'))
print(check_lisp_line('((if [a >) 1] println var)'))
print(check_lisp_line('(for-loop {[i 0 (< i 10)} [(inc i)]} (println i))'))
print(check_lisp_line('((if [a > 1] println var))'))


# stdout:
# True
# False
# False
# True


# ИТОГ: отлично! — 12/12
