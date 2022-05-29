import sys
input = sys.stdin.readline

S = set([])
m = int(input())
for _ in range(m):
    line = input().split()
    if len(line)==1:
        if line[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S.clear()
    else:
        if line[0] == 'add':
            S.add(int(line[1]))
        elif line[0] == 'remove':
            S.discard(int(line[1]))
        elif line[0] == 'check':
            if int(line[1]) in S:
                print(1)
            else:
                print(0)
        elif line[0] == 'toggle':
            if int(line[1]) in S:
                S.remove(int(line[1]))
            else:
                S.add(int(line[1]))