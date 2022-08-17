cnt = 0

for number in range(100, 1000):
    digit1 = number // 100
    digit2 = number // 10 % 10
    digit3 = number % 10
    if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
        cnt += 1

print(cnt)
