'''
확산은 모든 칸에서 동시에 일어남
공기 청정기가 있는 곳으로는 확산 안일어남
공기 청정기의 위치는 ((2, 0), (3, 0)) 으로 고정
'''

import sys; ssr = sys.stdin.readline

def diffusion(ap_pos, r, c):
    result = [[0 for _ in range(c)] for _ in range(r)]
    dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for cur_r in range(r):
        for cur_c in range(c):
            flag = 0
            if a[cur_r][cur_c] > 0:
                for dr, dc in dpos:
                    diffuse_r, diffuse_c = cur_r + dr, cur_c + dc
                    if 0 <= diffuse_r < r and 0 <= diffuse_c < c and a[diffuse_r][diffuse_c] != -1:
                        result[diffuse_r][diffuse_c] += a[cur_r][cur_c]//5
                        flag += 1
            result[cur_r][cur_c] += a[cur_r][cur_c] - a[cur_r][cur_c]//5*flag
    result[ap_pos[0]][0], result[ap_pos[1]][0] = -1, -1
    return result

def air_purifier(ap_pos, r, c):
    # up
    up_dpos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    up_pos = [ap_pos[0]-1, 0]
    cursor = 0
    while up_pos != [ap_pos[0], 0]:
        next_r, next_c = up_pos[0] + up_dpos[cursor][0], up_pos[1] + up_dpos[cursor][1]
        if 0 <= next_r <= ap_pos[0] and 0 <= next_c < c:
            a[up_pos[0]][up_pos[1]] = a[next_r][next_c]
            up_pos = [next_r, next_c]
        else:
            cursor += 1
    a[ap_pos[0]][1] = 0
    # down
    down_dpos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    down_pos = [ap_pos[1]+1, 0]
    cursor = 0
    while down_pos != [ap_pos[1], 0]:
        next_r, next_c = down_pos[0] + down_dpos[cursor][0], down_pos[1] + down_dpos[cursor][1]
        if ap_pos[1] <= next_r < r and 0 <= next_c < c:
            a[down_pos[0]][down_pos[1]] = a[next_r][next_c]
            down_pos = [next_r, next_c]
        else:
            cursor += 1
    a[ap_pos[1]][1] = 0
        
r, c, t = map(int, ssr().split())
a = [list(map(int, ssr().split())) for _ in range(r)]
ap_pos = []
for i in range(r):
    if a[i][0] == -1:
        ap_pos = [i, i+1]
        break
for _ in range(t):
    a = diffusion(ap_pos, r, c)
    air_purifier(ap_pos, r, c)
ans = 0
for i in range(r):
    for j in range(c):
        ans += a[i][j]
print(ans+2)

'''
8 8 10
7 6 5 4 3 2 1 2
8 0 0 0 0 0 0 3
9 0 0 0 0 0 0 4
-1 7 8 9 8 7 6 5
-1 7 8 9 8 7 6 5
9 0 0 0 0 0 0 4
8 0 0 0 0 0 0 3
7 6 5 4 3 2 1 2
'''