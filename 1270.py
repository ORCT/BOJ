import sys
from collections import defaultdict
ssr = sys.stdin.readline

n = int(ssr())
for _ in range(n):
    t = list(map(int, ssr().split()))
    cnt = defaultdict(int)
    sol = defaultdict(list)
    for i in range(1, len(t)):
        cnt[t[i]] += 1
    for key, value in cnt.items():
        sol[-value].append(key)
    for key, value in sorted(sol.items()):
        if -key > t[0]//2 and len(value) == 1:
            print(value[0])
            break
        else:
            print('SYJKGW')
            break

'''
보이어-무어 과반수 투표 알고리즘에 대해 찾아볼 것
'''