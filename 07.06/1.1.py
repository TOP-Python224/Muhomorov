import datetime as d

curr_year = d.datetime.now().year

f_name = input("Введите Ваше имя: ")
l_name = input("Введите Вашу фамилию: ")
bd_year = input("Введите год Вашего рождения: ")

print(f"{f_name} {l_name}, {curr_year - int(bd_year)}")