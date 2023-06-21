'''import sys

ssr = sys.stdin.readline

for _ in range(3):
    n = int(ssr())
    s = 0
    for _ in range(n):
        s += int(ssr())
    if s == 0:
        print('0')
    elif s < 0:
        print('-')
    else:
        print('+')'''
        
import sys

ssr = sys.stdin.readline

for _ in range(3):
    n = int(ssr())
    s = sum(int(ssr()) for _ in range(n))
    if s == 0:
        print('0')
    elif s < 0:
        print('-')
    else:
        print('+')