n = int(input())
dict = {}
for _ in range(n):
    a,b = input().split(' = ')
    dict[a] = b
t = int(input())
for _ in range(t):
    k = int(input())
    s = input().split()
    for i in s:
        print(dict[i], end = ' ')
    print()