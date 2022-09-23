n = int(input())
m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    n -= a*b
if n == 0:
    print('Yes')
else:
    print('No')