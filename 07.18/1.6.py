cnt = 0

for n in range(1000, 10000):
    n = str(n)
    if sum([0, 0, int(n[:1])]) == sum([int(n[1:2]), int(n[2:3]), int(n[3:4])]):
        cnt += 1
        
for n in range(10000, 100000):
    n = str(n)
    if sum([0, int(n[:1]), int(n[1:2])]) == sum([int(n[2:3]), int(n[3:4]), int(n[4:])]):
        cnt += 1

for n in range(100000, 1000000):
    n = str(n)
    if sum([int(n[:1]), int(n[1:2]), int(n[2:3])]) == sum([int(n[3:4]), int(n[4:5]), int(n[5:])]):
        cnt += 1
        
print(cnt)



