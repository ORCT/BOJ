import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

check_list=[]

for i in range(N):
    if A[i]-X<0:
        check_list.append(A[i])

for i in range(len(check_list)):
    print(check_list[i], end = ' ')