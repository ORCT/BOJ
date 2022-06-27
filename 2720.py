t = int(input())
d = [25,10,5,1]
for _ in range(t):
    c = int(input())
    ans = []
    for i in d:
        ans.append(c//i)
        c %= i
    print(*ans)