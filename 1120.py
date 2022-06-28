a,b = input().split()
ans = 50
for i in range(len(b)-len(a)+1):
    tmp = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            tmp += 1
    if tmp < ans:
        ans = tmp
print(ans)