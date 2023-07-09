'''
어느 칸에서 출발했는지를 알 수가 없다는게 어려운 점이 아닐까
미로의 크기도 안주어지고
직사각형이라 처음부터 배열을 만들어놓고 진행할수도 없고

모든 이동할 수 있는 칸을 걸었을 때의 기록이 입력이다 라는게 중요한 점으로 보인다.
이동 경로에 포함되지 않는 곳은 다 벽
'''

def f(mx, my):
    for i in range(my+1):
        for j in range(mx+1):
            labyrinth = [['#' for _ in range(mx+1)] for _ in range(my+1)]
            posx, posy = j, i
            labyrinth[posy][posx] = '.'
            for k in route:
                if 0 <= k[0] + posy <= my and 0 <= k[1] + posx <= mx:
                    labyrinth[posy+k[0]][posx+k[1]] = '.'
                else:
                    break
            else:
                return labyrinth
                
direction = [(1,0), (0,-1), (-1,0), (0,1)]
route = [(0,0)]
n = int(input())
log = input()
d = 0
pos = [0, 0]
for i in log:
    if i == 'R':
        d += 1
    elif i == 'L':
        d -= 1
    else:
        pos[0] += direction[d%4][0]
        pos[1] += direction[d%4][1]
        route.append((pos[0], pos[1]))
my = max([i[0] for i in route]) - min([i[0] for i in route])
mx = max([i[1] for i in route]) - min([i[1] for i in route])
ans = f(mx, my)

for i in ans:
    print(''.join(i))