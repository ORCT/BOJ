'''from collections import deque
import sys
ssr = sys.stdin.readline

def check_target(size):
    target = []
    pos = 0
    for i in range(n):
        for j in range(n):
            if t[i][j] == 9:
                pos = (i,j)
            elif t[i][j] > 0:
                target.append((i,j,t[i][j]))
    return pos, target

n = int(ssr())
t = [list(map(int, ssr().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque([])
dp = [(-1, 0), (0, -1), (0, 1), (1, 0)]
size = 2
pos, target = deque(check_target(size))
eat = 0
ans = 0
while target:
    destination = target.popleft()
    
    for i in dp:
        if 0 <= tmp[0] + i[0] < n and 0 <= tmp[1] + i[1] < n:
            if 0 < t[tmp[0] + i[0]][tmp[1] + i[1]] < size:
                q.append((tmp[0] + i[0], tmp[1] + i[1], tmp[2] + 1))
                t[tmp[0] + i[0]][tmp[1] + i[1]] = 0
                eat += 1
                if eat == size:
                    size += 1
                    eat = 0
                    pos, target = check_target(size)
            elif t[tmp[0] + i[0]][tmp[1] + i[1]] == 0:
                q.append((tmp[0] + i[0], tmp[1] + i[1], tmp[2] + 1))
                t[tmp[0] + i[0]][tmp[1] + i[1]] -= 1
                break
print(ans)     ''' 
'''
1원칙. 그때그때 제일 가까운 놈을 골라야한다. 근데 이걸 이동할 때 마다 할 수가 있냐
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다(먹을 때 마다 체크를 해야하나?)
물고기를 먹는 우선도는 가장 가까운 물고기, 그런 물고기가 많다면(다들 거리가 같다면) 가장 위에 있는 물고기, 모두 위에 있다면 가장 왼쪽
사이즈가 커졌더니 경로가 재설정되는 일도 있겠지
거리가 가까운 순으로 정렬을 해야하나...
bfs를 수행하는 것 자체가 가장 가까운 놈들부터 가는거임
즉 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기
미리 왼쪽 위 순서부터 q에다 넣으면 어떰?
q가 아니라 다른 자료여도 아무튼 표시를 하는게 좋을 것 같다
방문 처리를 잘 써야할듯
아예 안하자니 백퍼센트 메모리 문제랑 시간 문제가 생길거고
잘못했다가는 먹을 수 있는 물고기가 있음에도 가지못하거나 비효율적인 루트를 정하게 될 듯
일단 완벽한 케이스부터 짜보자
사방에 다 먹을 수 있는게 있을 경우 데이터가 꼬인다
한 쪽을 선택하면 반복을 취소?
그랬을 때 그게 최선의 선택이 아니라면? 가령 맨 처음 선택했을 때는 연속 2개만 먹는데 다른 길을 선택했다면 연속해서 그보다 많이 먹을 수 있다면
이동거리 대비 시간이 많이 걸린 경우를 배제한다면?(이동거리는 처음 시작한 좌표랑 현재 위치랑 비교)

1. 모든 물고기는 상어보다 작다(1이다), 빈칸은 없다

일단 처음에 타겟의 위치를 다 잡아두는게 좋을 것 같은게,
bfs를 수행해서 주변에 있는 애들을 다 먹었는데 만약에 저 멀리에 하나가 남아있다면?
0일 때는 일반적인 bfs를 하면서 그래프 탐색을 진행한다면? 메모리 초과는 어떻게 해결?
괜히 처음에 n^2 쉽게 넘기려다가 오히려 더 어렵게 가는 길이 아닐까 싶은데
처음에 n^2으로 돌아 그 다음에 그게 들어 있는 리스트에서 값을 바꾸면서(9 위치랑 대조해서 거리를 체크하는거지)
거리 체크해서 우선 순위를 좀 짜보면? 

'''
from collections import deque
import sys
ssr = sys.stdin.readline

def bfs():#n^2 - 1 돌면서 현재 상태에서 먹을 수 있는 물고기를 전부 추가
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while q:
        tmp = q.popleft()
        visited[tmp[0]][tmp[1]] = 1
        for i in dp:
            if 0 <= tmp[0] + i[0] < n and 0 <= tmp[1] + i[1] < n:#테이블 범위를 벗어나지 않을 때
                if t[tmp[0] + i[0]][tmp[1] + i[1]] <= size and visited[tmp[0] + i[0]][tmp[1] + i[1]] == 0:#이동이 가능할 때
                    visited[tmp[0] + i[0]][tmp[1] + i[1]] = 1#이동했다
                    if 0 < t[tmp[0] + i[0]][tmp[1] + i[1]] < size:#먹을 수 있을 때
                        fish_list.append((tmp[0] + i[0], tmp[1] + i[1], tmp[2]+1))#물고기 리스트에 추가
                    else:#못먹거나 0일 때
                        q.append((tmp[0] + i[0], tmp[1] + i[1], tmp[2] + 1))#이동했다고치고 bfs를 위해 추가
    
def eat_fish():
    global size, eat, fish, ans
    if len(fish_list) == 0:
        fish = 0#fish_list가 비었다는 건 먹을 수 있다는게 없다는 뜻, 반복문을 끝내기 위해 0으로
        return
    fish_list.sort(key = lambda x:(x[2],x[0],x[1]))
    tmp = fish_list.pop(0)
    q.append(tmp)
    eat += 1
    fish -= 1
    ans = tmp[2]
    if size == eat:
        size += 1
        eat = 0
    t[tmp[0]][tmp[1]] = 0
        
n = int(ssr())
t = [list(map(int, ssr().split())) for _ in range(n)]
q = deque([])
fish = 0
for i in range(n):
    for j in range(n):
        if t[i][j] == 9:
            q.append((i,j,0))
            t[i][j] = 0
        elif t[i][j] > 0:
            fish += 1
dp = [(-1, 0), (0, -1), (0, 1), (1, 0)]
size = 2
eat = 0
ans = 0
while fish > 0:
    fish_list = []
    bfs()
    eat_fish()
print(ans)

'''시작할 때의 좌표에서 먹을 수 있는 모든 물고기를 찾은 다음에 거기서 제일 가깝고, 제일 위에있고, 제일 왼쪽에 있는 놈 하나만 먹고 위치를 그쪽으로 옮겨
이러면 방문처리를 해도 아무런 문제가 없어지지
'''