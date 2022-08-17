n = int(input())
prv = 0
nxt = 1

for i in range(n):
    prv, nxt = nxt, nxt + prv
    print(prv, end=' ')
    
        
        