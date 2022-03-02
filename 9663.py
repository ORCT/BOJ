import sys
ssr = sys.stdin.readline

def put_queen(cdx):
    if cdx == n:
        global cnt
        cnt += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            q_list[cdx] = i
            if check(cdx):
                visited[i] = True
                put_queen(cdx+1)
                visited[i] = False
            
def check(n):
    for i in range(n):
        if q_list[n] == q_list[i] or n-i == abs(q_list[n] - q_list[i]):
            return False
    return True
                
if __name__ == '__main__':
    n = int(ssr())
    cnt = 0
    q_list = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    
    put_queen(0)
    print(cnt)