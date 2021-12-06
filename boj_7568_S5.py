t = int(input())
a = []
for i in range(t):
    a.append(input().split())
seq = []
for i in range(len(a)):
    cnt = 1
    for j in range(len(a)):
        if int(a[i][0]) < int(a[j][0]) and int(a[i][1]) < int(a[j][1]):
            cnt += 1
    seq.append(cnt)
print(*seq)