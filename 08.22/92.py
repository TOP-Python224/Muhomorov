months = {  1: 31, 2: 28, 3: 31,
            4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31 } 
warranty = 180

def yearIsLeap(year: int) -> bool:
    """Функция принимает на вход год и возвращает True, если год високосный, и False, если нет.
       Также, если год високосный - модифицирует количество дней февраля в словаре months."""
    if not year % 4 and year % 100 or not year % 400:
        months[2] = 29
        return True
    else:
        return False
    
def realDate(year: int, days: int) -> int:
    """Функция принимает на вход год и порядковый номер дня, и возвращает дату."""
    isleap = yearIsLeap(year)
    for m in months:
        if days <= months[m]:
            return f"{days:02}-{m:02}-{year}"
        else:
            days -= months[m]
   
year = int(input('Введите год покупки телевизора: '))
days = int(input('Введите порядковый номер дня покупки телевизора: '))

isleap = yearIsLeap(year)
if (isleap and 0 < days <= 366) or (not isleap and 0 < days <= 365):
    end_day = days + warranty
    if isleap and end_day > 366:
        year += end_day // 366
        days = end_day - 366
    elif not isleap and end_day > 365:
        year += end_day // 365
        days = end_day - 365
    print(f"Дата окончания гарантии на телевизор - {realDate(year, days)}")
else:
    print("Введено неправильное количество дней!")

# Введите год покупки телевизора: 2019
# Введите порядковый номер дня покупки телевизора: 300
# Дата окончания гарантии на телевизор - 24-04-2020

# Введите год покупки телевизора: 2019
# Введите порядковый номер дня покупки телевизора: 366
# Введено неправильное количество дней!

# Введите год покупки телевизора: 2020
# Введите порядковый номер дня покупки телевизора: 366
# Дата окончания гарантии на телевизор - 28-06-2021