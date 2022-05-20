t = int(input())
sub = [0 for _ in range(1000)]
sub1 = [0 for _ in range(1000)]
for i in range(1,1000):
    sub[i] = sub[i-1]+i
    sub1[i] = sub1[i-1]+sub[i]
for i in range(t):
    n = int(input())
    print(f'{i+1}: {n} {sub1[n]}')
    
#1,3,6,10,15,21
#1,4,10,20,35