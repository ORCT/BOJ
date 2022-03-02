import sys
ssr = sys.stdin.readline

n = int(ssr())
num = list(map(int, ssr().split()))
sorted_num = sorted(list(set(num)))
dict = {sorted_num[i] : i for i in range(len(sorted_num))}
for i in num:
    print(dict[i], end = ' ')