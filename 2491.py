n = int(input())
num = list(map(int, input().split()))
inc = 1
dec = 1
tmp = 1
for i in range(len(num)-1):
    if num[i] <= num[i+1]:
        tmp += 1
    else:
        inc = max(inc, tmp)
        tmp = 1
inc = max(inc, tmp)
tmp = 1
for i in range(len(num)-1):
    if num[i] >= num[i+1]:
        tmp += 1
    else:
        dec = max(dec, tmp)
        tmp = 1
dec = max(dec, tmp)
print(max(inc, dec))