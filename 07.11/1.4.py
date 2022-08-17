a, b, c = input('Введите 3 числа через пробел: ').split(' ')
a, b, c = int(a), int(b), int(c)
sum = 0

if a > 0: sum += a
if b > 0: sum += b
if c > 0: sum += c 

print(sum)
