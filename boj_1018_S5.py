import sys

N,M = map(int, input().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline().rstrip())
min_list = []
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i,i+8):
            tmp1 = 0
            tmp2 = 0
            for l in range(j,j+8):
                if board[k][l] == "W":
                    tmp1 += 1
                if board[k][l] == 'B':
                    tmp2 += 1
            cnt1 += abs(4-tmp1)
            cnt2 += abs(4-tmp2)
        min_list.append(min(cnt1,cnt2))
print(board)
print(min_list)
print(min(min_list))