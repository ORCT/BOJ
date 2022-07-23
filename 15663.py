'''import sys
ssr = sys.stdin.readline

def sol():
    if len(ans) == m:
        print(*ans)
        return
    last = 0
    for i in range(n):
        if visited[i] == 0 and last != num[i]:
            visited[i] = 1
            ans.append(num[i])
            last = num[i]
            sol()
            ans.pop()
            visited[i] = 0

n,m = map(int, ssr().split())
num = sorted(list(map(int, ssr().split())))
visited = [0 for _ in range(n)]
ans = []
sol()'''
'''
모든 출력했던 수열을 저장해놨다가 출력할 때 마다 비교하는 건 시간초과나서 못해
숫자 구분용이랑, 리얼 방문용이랑 두 개 만들어서 둘 다 방문처리 해주면 어찌어찌 해볼만 할듯
'''

from itertools import permutations
import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
num = sorted(list(map(int, ssr().split())))
ans = list(set(permutations(num, m)))
ans.sort()
for i in ans:
    print(*i)