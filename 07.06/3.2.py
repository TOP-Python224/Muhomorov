number = input("Введите число из 4-х цифр: ")

res_mult = 1

for i in number:
    res_mult *= int(i)
    
print(f'Результат - {res_mult}')