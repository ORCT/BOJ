t = int(input())
point = []
for i in range(t):
    point.append(input().split())
point.sort(key = lambda x : (int(x[1]), int(x[0])))
for i in range(t):
    print(f'{point[i][0]} {point[i][1]}')