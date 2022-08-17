numbers = ''

while True:
    n = int(input())
    numbers = numbers + str(n) + ' ' 
    if n % 7 != 0:
        break 

print(numbers)
