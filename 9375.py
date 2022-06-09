t = int(input())
for _ in range(t):
    n = int(input())
    cl = [input().split() for _ in range(n)]
    c = {i[1]:[] for i in cl}
    ans_l = []
    for i in cl:
        c[i[1]].append(i[0])
    for i in c.keys():
        ans_l.append(len(c[i]))
    ans = 1
    for i in ans_l:
        ans *= i+1
    print(ans-1)