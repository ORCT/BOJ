import sys
ssr = sys.stdin.readline

def cow(n,m,cnt,ans):
    if n%2 == 1 and m%2 == 1:
        ans += cnt
        cnt *= 4
        cow(n//2,m//2,cnt,ans)
    else:
        print(ans)
        return

n,m = map(int, ssr().split())# n = row, m = col 더이상 나눠지지 않거나 센터를 잡을 수 없을 떄까지 재귀 진행

cow(n,m,1,0)