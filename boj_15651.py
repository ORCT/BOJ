import sys
ssr = sys.stdin.readline

n,m = map(int,ssr().split())
check_list = [False for _ in range(n+1)]
arr = []
arr_len = 0

def func(arr_len):
    if arr_len == m:
        print(*arr)
        return
    for i in range(1,n+1):
        if not check_list[i]:
            arr.append(i)
            func(arr_len+1)
            arr.pop()
            
func(arr_len)