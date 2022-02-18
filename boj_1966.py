import sys
ssr = sys.stdin.readline

c = int(ssr())
for i in range(c):
    n,m = map(int, ssr().split())#문서의 갯수 n, 궁금한게 왼쪽 몇 번째에 있는지 m
    imp = list(map(int, ssr().split()))#n개 문서의 중요도가 차례대로 주어짐
    cnt = 0
    for j in range(n):
        idx = imp.index(max(imp))
        if idx <= m:
            _=1
        else:
            m += len(imp)
        imp.extend(imp[0:idx])
        del imp[0:idx]
        m -= idx
        imp.pop(0)
        m -= 1
        cnt += 1#원소가 아니라 원래 원소의 위치를
        if m == -1:
            print(cnt)
            break