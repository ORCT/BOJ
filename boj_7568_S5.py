t = int(input())
a = []
for i in range(t):
    a.append(input().split())
a_len = len(a)
seq = []
for i in range(a_len):
    cnt = 1
    for j in range(a_len):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1
    seq.append(cnt)
for i in seq:
    print(i, end=' ')