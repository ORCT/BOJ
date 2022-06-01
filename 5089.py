'''cnt = 0
while 1:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    t = set([input() for _ in range(n)])
    print(f'Week {cnt} {len(t)}')'''
    
cnt = 0
while 1:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    t = {input():1 for _ in range(n)}
    print(f'Week {cnt} {len(t.keys())}')
#Week n주차 실제로 들러야 하는 타운 갯수
#set으로 쉽게 구현 가능