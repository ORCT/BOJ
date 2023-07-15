import sys
ssr = sys.stdin.readline

def is_available_a(points, x, y, l):
    for i in points:
        if min(x, x+l) <= i[0] <= max(x, x+l) and (i[1] == y or i[1] == y+l):
            continue
        elif (i[0] == x or i[0] == x+l) and min(y, y+l) <= i[1] <= max(y, y+l):
            continue
        else:
            return False
    else:
        return True
    
def is_available_b(points, x, y, l):
    for i in points:
        if x-l <= i[0] <= x and (i[1] == y or i[1] == y+l):
            continue
        elif (i[0] == x-l or i[0] == x) and y <= i[1] <= y+l:
            continue
        else:
            return False
    else:
        return True
    
def is_available_c(points, x, y, l):
    for i in points:
        if x <= i[0] <= x+l and (i[1] == y-l or i[1] == y):
            continue
        elif (i[0] == x or i[0] == x+l) and y-l <= i[1] <= y:
            continue
        else:
            return False
    else:
        return True
    
def is_available_d(points, x, y, l):
    for i in points:
        if x-l <= i[0] <= x and (i[1] == y-l or i[1] == y):
            continue
        elif (i[0] == x-l or i[0] == x) and y-l <= i[1] <= y:
            continue
        else:
            return False
    else:
        return True
    
n = int(ssr())
points = [list(map(int, ssr().split())) for _ in range(n)]
minx, miny = min([points[i][0] for i in range(n)]), min([points[i][1] for i in range(n)])
maxx, maxy = max([points[i][0] for i in range(n)]), max([points[i][1] for i in range(n)])
l = max(maxx - minx, maxy - miny)
    
if is_available_a(points, minx, miny, l) or is_available_a(points, maxx, miny, l) or is_available_a(points, minx, maxy, l) or is_available_a(points, maxx, maxy, -l):
    print(l)
else:
    print(-1)
    
'''
시작 위치를 컨트롤 하는 방법 말고 다른게 필요한데
4
0 1
0 2
0 3
-1 3
이런 반례를 잡아내지를 못함
음수를 상정하고 만든게 아니라서'''