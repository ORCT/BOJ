from collections import deque
import sys
ssr = sys.stdin.readline

t = int(ssr())
for _ in range(t):
    p = ssr().rstrip()
    n = int(ssr())
    state = 1
    if n == 0:
        num = ssr().rstrip()
        num = deque([])
    else:
        num = ssr().rstrip()
        num = deque(num[1:-1].split(','))
    for i in p:
        if i == 'R':
            state *= -1
        else:
            if len(num) == 0:
                state = 0
                break
            else:
                if state == 1:
                    num.popleft()
                else:
                    num.pop()
    if state == 1:
        ans = '[' + ','.join(num) + ']'
        print(ans)
    elif state == -1:
        num.reverse()
        ans = '[' + ','.join(num) + ']'
        print(ans)
    else:
        print('error')