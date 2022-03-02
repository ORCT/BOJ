import sys
ssr = sys.stdin.readline

N, M = map(int, ssr().split())
check_list = [False for _ in range(N + 1)]
arr = []
arr_len = 0

def func(arr_len):
    if arr_len == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if not check_list[i]:
            arr.append(i)
            check_list[i] = True
            func(arr_len + 1)
            arr.pop()
            check_list[i] = False

func(0)