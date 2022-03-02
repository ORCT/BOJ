import sys
ssr = sys.stdin.readline

def func():
    cnt = [0 for i in range(20000001)]
    for i in num:
        cnt[i+10000000] += 1
    for i in mnum:
        print(cnt[i+10000000],end=' ')

n=ssr()
num=list(map(int, ssr().split()))
m=ssr()
mnum=list(map(int, ssr().split()))

func()