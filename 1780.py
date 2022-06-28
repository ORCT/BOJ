import sys
ssr = sys.stdin.readline

def sol(r,c,l):
    tmp = p[r][c]
    for i in range(r,r+l):
        for j in range(c,c+l):
            if tmp != p[i][j]:
                le = l//3
                for k in range(3):
                    for h in range(3):
                        sol(r+k*le,c+h*le,le)
                return
    if tmp == -1:
        ans[0] += 1
    elif tmp == 0:
        ans[1] += 1
    else:
        ans[2] += 1

n = int(ssr())
p = [list(map(int, ssr().split())) for _ in range(n)]
ans = [0,0,0]
sol(0,0,n)
print(f'{ans[0]}\n{ans[1]}\n{ans[2]}')