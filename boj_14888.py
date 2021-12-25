import sys
ssr = sys.stdin.readline

def func():
    if cnt == len(num)-1:
        result_list.append(result)
    for i in range(len(check)):
        check[i] = True
        

n = int(ssr())
num = list(map(int, ssr().split()))
oper = list(map(int, ssr().split()))
check = [False for _ in range(len(num)-1)]