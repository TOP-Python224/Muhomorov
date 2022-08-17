cnt = 0

for number in range(100, 10000):
    if number < 1000:
        digit1 = number // 100
        digit2 = number // 10 % 10
        digit3 = number % 10
        if digit1 != digit2 and digit1 != digit3 and digit2 != digit3:
            cnt += 1
    else:
        digit1 = number // 1000
        digit2 = number // 100 % 10
        digit3 = number // 10 % 10
        digit4 = number % 10
        if (digit1 != digit2 and digit1 != digit3 and digit1 != digit4
            and digit2 != digit3 and digit2 != digit4 
            and digit3 != digit4):
            cnt += 1

print(cnt)
