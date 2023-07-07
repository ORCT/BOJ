# import sys
# from collections import defaultdict
# ssr = sys.stdin.readline

# n = int(ssr())
# for _ in range(n):
#     t = list(map(int, ssr().split()))
#     cnt = defaultdict(int)
#     sol = defaultdict(list)
#     for i in range(1, len(t)):
#         cnt[t[i]] += 1
#     for key, value in cnt.items():
#         sol[-value].append(key)
#     for key, value in sorted(sol.items()):
#         if -key > t[0]//2 and len(value) == 1:
#             print(value[0])
#             break
#         else:
#             print('SYJKGW')
#             break

'''
보이어-무어 과반수 투표 알고리즘에 대해 찾아볼 것

과반수 후보를 기록하고 같은게 나오면 카운트를 하나 올리고
다른게 나오면 카운트를 하나 내리는데
0개일 때 다른게 나오면 과반수 후보를 교체
그렇게 해서 마지막에 남은 녀석이 과반수 후보
근데 순서에 따라 마지막에 남는게 달라질 수 있으므로
후보 선출이 끝나고 진짜로 과반수가 넘는지 확인하는 과정 필요
- 왜 한 번 더 확인하는 과정이 필요할까?
1122333 이런 입력이 주어지면 major = 3, cnt = 1이지만 실제로 3은 3/7로 과반수가 되지 않기 때문
'''

import sys
ssr = sys.stdin.readline

def boyer_moore_majority(t):
    major = 0
    cnt = 0
    for i in range(1, len(t)):
        if cnt == 0:
            major = t[i]
            cnt += 1
        else:
            if t[i] == major:
                cnt += 1
            else:
                cnt -= 1
    check = t[1:].count(major)
    if check > t[0]//2:
        print(major)
    else:
        print('SYJKGW')

n = int(ssr())
for _ in range(n):
    t = list(map(int, ssr().split()))
    ans = boyer_moore_majority(t)