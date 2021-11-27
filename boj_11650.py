n = int(input())
point = []
for i in range(n):
    point.append(input().split())
point.sort(key = lambda x : (int(x[0]),int(x[1])))
for i in range(n):
    for j in range(2):
        print(point[i][j], end = ' ')
    print()