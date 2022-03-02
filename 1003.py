'''
First : just recursive

import sys
ssr = sys.stdin.readline

def fibonacci(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(ssr())
cnt0 = 0
cnt1 = 0
for i in range(n):
    fibonacci(int(ssr()))
    print(cnt0,cnt1)
    cnt0 = 0
    cnt1 = 0
'''
#모든 숫자에 대한 모든 값을 다 미리 집어 넣는 것을
#호출에 호출에 호출을 거듭해서 처음부터 해오는거지
import sys
ssr = sys.stdin.readline

n = int(ssr())
cnt0 = [0 for _ in range(41)]
cnt1 = [0 for _ in range(41)]
cnt0[0] = 1
cnt0[1] = 0
cnt1[0] = 0
cnt1[1] = 1
for i in range(2,41):
    cnt0[i] = cnt0[i-1] + cnt0[i-2]
    cnt1[i] = cnt1[i-1] + cnt1[i-2]
for i in range(n):
    a = int(ssr())
    print(f'{cnt0[a]} {cnt1[a]}')