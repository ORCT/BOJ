'''
예전에 풀었던 dp 타일 문제랑 흡사해 보임
파이프는 항상 빈칸만 차지할 수 있다
파이프는 →, ↘, ↓ 방향이 가능함
파이프는 밀어서 이동하기 때문에 최소 1칸이 이전 위치와 겹침
회전도 가능하다(45도, 단 미는 중에만 회전가능)

파이프의 시작 위치는 ((0, 0), (0, 1))
집의 크기 3 <= N <= 16
빈 칸 : 0, 벽 : 1

파이프의 한 쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력
이동시키지 못할 경우는 0을 출력
이동 방법은 최대 1,000,000
'''

'''
입력
3
0 0 0
0 0 0
0 0 0

파이프가 있는 위치를 2라고 하면,

1.
2 2 0
0 0 0
0 0 0

2.
0 2 0
0 0 2
0 0 0

3.
0 0 0
0 0 2
0 0 2

이렇게 3번만에 (2, 2) 까지 이동이 가능하고(입력 n으로 주는거 그대로 쓰지 말고 나중에 1빼주고)
다른 방법은 없으니까 답은 1

아니면 이렇게 말고 시작 위치를 (0, 1)로 하고 1칸씩 이동하는 방법으로 케이스를 줄이면?
왼쪽 위에서 오른쪽 아래로 가는거니까(애초에 조건에 오른, 오른아래, 아래 밖에 선택지가 없다)
뒤로는 못감

그럼 케이스를 3가지로 하고 (이전에 이동했던 방법에 따라 다음 이동에 제약이 생긴다)

밀면서 이동해야 하기 때문에 진행방향에 벽이 있으면 아예 진행을 못한다

2 2 1
0 0 0
0 0 0 이면 이동 불가능

2 2 0
0 0 1
0 0 0 이면? (0, 1) 이동은 가능한가

2 0 0
0 2 0
0 0 1 이면

파이프의 현재 위치에서 같은 방향에 벽이 있으면 진행 불가
이거랑 보드 밖으로 못나가게 하는걸 어떻게 같이 체크하지
'''

'''
# DFS

import sys; ssr = sys.stdin.readline

def f(cur_r, cur_c, cur_dir):
    global ans
    if cur_r == n-1 and cur_c == n-1:
        ans += 1
        return
    else:
        if cur_dir == 0 or cur_dir == 1:
            if cur_c+1 < n and board[cur_r][cur_c+1] != 1:
                f(cur_r, cur_c+1, 0)
        if cur_dir == 1 or cur_dir == 2:
            if cur_r+1 < n and board[cur_r+1][cur_c] != 1:
                f(cur_r+1, cur_c, 2)
        if cur_r+1 < n and cur_c+1 < n and board[cur_r+1][cur_c+1] != 1 and board[cur_r][cur_c+1] != 1 and board[cur_r+1][cur_c] != 1:
            f(cur_r+1, cur_c+1, 1)
                        
n = int(ssr())
board = [list(map(int, ssr().split())) for _ in range(n)]
board[0][0], board[0][1] = 2, 2
ans = 0
f(0, 1, 0)
print(ans)
'''

'''
그래서 이걸 dp로 풀면 어떻게 되려나
오른쪽 아래를 기준으로 잡고 3x3, 4x4, 5x5 이렇게 나가야 하나
벽은 어떻게 해야하지

이 문제에서 dp table 의 의미 : 현재 칸을 끝으로 하는 가로, 세로, 대각선의 파이프 개수
초기 상태를 예로 들면 dp[0][1] = [1, 0, 0] # 가로, 대각, 세로 순서일 때
이렇게 쓸 수 있다는 얘기
3차원 dp라니 이건 진짜 처음이네

반복문을 사용하고 이전 노드의 값을 활용하면 지금 노드의 값을 채울 수 있음
예를 들어 가로 파이프의 경우 직전 파이프가 가로거나 대각선인 경우 둘 다 가능
따라서 dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j-1][1] 이런식으로 점화식을 작성할 수 있을 듯'''

# DP : 모든 경우를 다 돌려보고 최선의 경우를 저장

import sys; ssr = sys.stdin.readline

n = int(ssr())
board = [list(map(int, ssr().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(2, n):
        if board[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        if board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
        dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[n-1][n-1]))