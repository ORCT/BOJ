import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
check_list = [False for _ in range(n+1)]
arr = []
arr_len = 0
num=1

def func(num, arr_len):
    if arr_len == m:
        print(*arr)
        return
    for i in range(num,n+1):
        if not check_list[i]:
            arr.append(i)
            func(i,arr_len + 1)
            arr.pop()
            
func(num, arr_len)