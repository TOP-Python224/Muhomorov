n = int(input())
sum = n

for i in range(1, n):
    if not n % i:
        sum += i

print(sum)
  
