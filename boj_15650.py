import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
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
            check_list[i] = True
            func(arr_len + 1)
            arr.pop()
            check_list[i] = False
            
func(arr_len)
#일단 리스트 같은 자료형에다 추가한 다음에 조건에 맞으면 출력하도록 하는 형태는 기본으로 깔아야 함
#여기서 수열끼리의 중복도 지우는 것이다