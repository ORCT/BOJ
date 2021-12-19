import sys
ssr = sys.stdin.readline

def counting():
    cnt = [0 for _ in range(1,100002)]
    for i in num:
        cnt[i] += 1
    for j in num1:
        if cnt[j] == 0:
            print(0)
        else:
            print(1)
    return
            
n = int(ssr())
num = list(map(int, ssr().split()))
m = int(ssr())
num1 = list(map(int, ssr().split()))

counting()