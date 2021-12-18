import sys
ssr = sys.stdin.readline

n = int(ssr())
q_list = []#index is row, element is column

def put_queen(n,cnt):
    for i in range(1,n+1):
        if len(q_list)==n:
            cnt += 1
        else:
            q_list.append(i)
            put_queen(n,cnt)
            q_list.pop()
    return cnt
            
cnt = put_queen(n,0)
print(cnt)