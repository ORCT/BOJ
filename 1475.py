from math import ceil
d = {i:0 for i in range(9)}
s = input()
s=s.replace('9','6')
for i in s:
    d[int(i)] += 1
d[6]=ceil(d[6]/2)
ans=0
for key, value in d.items():
    if value > ans:
        ans = value
print(ans)