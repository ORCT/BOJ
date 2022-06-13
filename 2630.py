import sys
ssr = sys.stdin.readline

def sol(r,c,length):
    global paper_cnt, blue_cnt
    std = 0
    color_cnt = 0
    for i in range(r,r+length):
        for j in range(c,c+length):
            std += 1
            color_cnt += b[i][j]
    if std == color_cnt or color_cnt == 0:
        paper_cnt += 1
        blue_cnt += color_cnt//std
        return
    else:
        #if length > 1:
        length //= 2
        sol(r,c,length)
        sol(r,c+length,length)
        sol(r+length,c,length)
        sol(r+length,c+length,length)

n = int(ssr())
b = [list(map(int, ssr().split())) for _ in range(n)]
paper_cnt = 0
blue_cnt = 0
sol(0,0,n)
print(paper_cnt-blue_cnt)
print(blue_cnt)