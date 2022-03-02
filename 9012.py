import sys
ssr = sys.stdin.readline

def func(s):
    if s.find('()')== -1:
        print('NO')
        return
    elif s == '()':
        print('YES')
        return
    if len(s)>=3:
        func(s.replace('()',''))

n = int(ssr())
for i in range(n):
    func(ssr().rstrip())