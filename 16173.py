#이동 가능한 건 딱 한순간에 선택한 방향과 칸수만큼만 이동가능

import sys
sys.setrecursionlimit(10000)

def sol(r,c):
    global cnt
    if r >= n or c >= n:
        return
    if b[r][c] == -1:
        cnt += 1
        return
    if b[r][c] == 0:
        return
    sol(r+b[r][c],c)
    sol(r,c+b[r][c])
n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]   
cnt = 0

sol(0,0)

if cnt >= 1:
    print('HaruHaru')
else:
    print('Hing')