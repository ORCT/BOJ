import sys
T = int(input())
for i in range(T):
    line=list(map(int, sys.stdin.readline().split()))
    H = line[0]
    W = line[1]
    N = line[2]
    Y = N%H
    if Y == 0:
        Y = str(H)
        X = N//H
    else:
        Y = str(N%H)
        X = 1 + (N//H)
    if X < 10:
        X = '0'+str(X)
    else:
        X = str(X)
    print(Y+X)