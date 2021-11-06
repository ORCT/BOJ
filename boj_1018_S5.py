import sys

N,M = map(int, input().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline())
print(board)