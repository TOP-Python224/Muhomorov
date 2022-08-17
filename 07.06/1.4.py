number = input("Введите целое положительное число: ")
res_sum, res_mult = 0, 1

for i in number:
    res_sum += int(i)
    res_mult *= int(i)
    
print(f"Сумма цифр = {res_sum}")
print(f"Произведение цифр = {res_mult}")


