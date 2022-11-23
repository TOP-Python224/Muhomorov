from datetime import date, datetime, timedelta
from math import ceil
from itertools import pairwise, count
from time import perf_counter


def str_to_date(str_date: str) -> date:
    """Преобразует строку с датой в формате ДД/ММ/ГГГГ в объект date."""
    d, m, y = str_date.split('/')
    return date(int(y), int(m), int(d))
# КОММЕНТАРИЙ: всё это очень хорошо, но у класса datetime есть классовый метод strptime(), который возвращает datetime объект из строки согласно переданному формату: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


# ИСПОЛЬЗОВАТЬ: отдельные переменные типов для вложенных аннотаций
CalendarPeriod = tuple[datetime, datetime]
CalendarPeriods = tuple[CalendarPeriod, ...]
def str_to_tuple(str_date_periods: str) -> CalendarPeriods:
    """Преобразует строку с периодами в формате ДД/ММ/ГГГГ-ДД/ММ/ГГГГ, ДД/ММ/ГГГГ-ДД/ММ/ГГГГ в кортеж со вложенными кортежами объектов datetime, соответствующим периодам."""
    periods_tuple = ()
    for periods in str_date_periods.split(','):
        dates_tuple = ()
        for dates in periods.split('-'):
            dates_tuple += (str_to_date(dates),)
        periods_tuple += (dates_tuple,)
    return periods_tuple


begin_date = input('Введите дату начала занятий в формате ДД/ММ/ГГГГ: ')
pairs = input('Введите количество пар: ')
pairs_per_day = input('Введите количество пар в день: ')
days_in_week = input('Введите учебные дни недели от 0 (Пнд) до 6 (Вск) через запятую: ')
vacations = input('Введите периоды каникул в формате ДД/ММ/ГГГГ-ДД/ММ/ГГГГ через запятую: ')
# vacations = '01/08/2022-14/08/2022, 31/12/2022-08/01/2023'

begin_date = str_to_date(begin_date)
vacations = str_to_tuple(vacations)
days_in_week = tuple([int(n) for n in days_in_week.split(',')])
study_days = ceil(int(pairs) / int(pairs_per_day))

# start = perf_counter()
#
# study_cnt = 0
# for period in vacations:
#     end_date = period[0]
#     study_period = (end_date - begin_date).days
#     for day in range(study_period):
#         curr_date = begin_date + timedelta(days=day)
#         if curr_date.weekday() in days_in_week:
#             print(f"{curr_date.strftime('%d/%m/%Y')}")
#             study_cnt += 1
#     begin_date = period[1]
# study_days -= study_cnt
#
# day = 1
# while study_days > 0:
#     curr_date = begin_date + timedelta(days=day)
#     if curr_date.weekday() in days_in_week:
#         print(f"{curr_date.strftime('%d/%m/%Y')}")
#         study_days -= 1
#     day += 1
#
# end = perf_counter()
# print(f"Elapsed time for 'days'-way: {end - start}")


# ИСПОЛЬЗОВАТЬ: такой вариант мне представляется всё-таки более упорядоченным с точки зрения потока выполнения — а по времени получается примерно одинаково

def is_vacation(lesson_date: date | datetime) -> bool:
    """Проверяет переданный день, попадает ли он в любой из заявленных периодов каникул."""
    for period_start, period_end in vacations:
        if period_start <= lesson_date <= period_end:
            return True
    return False

start = perf_counter()

# КОММЕНТАРИЙ: сдвиг (количество дней) относительно дня недели стартовой даты
week_shift = [0] + [d2-d1 for d1, d2 in pairwise(days_in_week)]
# study_weeks = ceil(study_days / len(days_in_week))

days = ()
# for i in range(study_weeks):
for i in count(0):
    for ws in week_shift:
        day = begin_date + timedelta(weeks=i) + timedelta(days=ws)
        if is_vacation(day):
            continue
        days += (day,)
    if len(days) >= study_days:
        break

for day in days:
    print(f'{day:%d/%m/%Y}')

end = perf_counter()
print(f"Elapsed time for 'weeks'-way: {end - start}")

# stdout:
# Введите дату начала занятий в формате ДД/ММ/ГГГГ: 04/07/2022
# Введите количество пар: 140
# Введите количество пар в день: 2
# Введите учебные дни недели от 0 (Пнд) до 6 (Вск) через запятую: 0, 2
# Введите периоды каникул в формате ДД/ММ/ГГГГ-ДД/ММ/ГГГГ через запятую: 01/08/2022-14/08/2022, 31/12/2022-08/01/2023
# 04/07/2022
# 06/07/2022
# 11/07/2022
# 13/07/2022
# 18/07/2022
# 20/07/2022
# 25/07/2022
# 27/07/2022
# 15/08/2022
# 17/08/2022
# 22/08/2022
# 24/08/2022
# 29/08/2022
# 31/08/2022
# 05/09/2022
# 07/09/2022
# 12/09/2022
# 14/09/2022
# 19/09/2022
# 21/09/2022
# 26/09/2022
# 28/09/2022
# 03/10/2022
# 05/10/2022
# 10/10/2022
# 12/10/2022
# 17/10/2022
# 19/10/2022
# 24/10/2022
# 26/10/2022
# 31/10/2022
# 02/11/2022
# 07/11/2022
# 09/11/2022
# 14/11/2022
# 16/11/2022
# 21/11/2022
# 23/11/2022
# 28/11/2022
# 30/11/2022
# 05/12/2022
# 07/12/2022
# 12/12/2022
# 14/12/2022
# 19/12/2022
# 21/12/2022
# 26/12/2022
# 28/12/2022
# 09/01/2023
# 11/01/2023
# 16/01/2023
# 18/01/2023
# 23/01/2023
# 25/01/2023
# 30/01/2023
# 01/02/2023
# 06/02/2023
# 08/02/2023
# 13/02/2023
# 15/02/2023
# 20/02/2023
# 22/02/2023
# 27/02/2023
# 01/03/2023
# 06/03/2023
# 08/03/2023
# 13/03/2023
# 15/03/2023
# 20/03/2023
# 22/03/2023

# Elapsed time for 'days'-way: 0.0011960000001636217
# Elapsed time for 'weeks'-way: 0.0011500999999043415


# ИТОГ: хорошо — 8/10
