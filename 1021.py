'''
양방향 순환? 큐 : 데크는 데크인데 순환?
1. 첫번째 원소를 뽑는다(항상 왼쪽 첫번째를 말하는게 아닌듯) popleft
2. 1을 뽑아서 맨 오른쪽으로 보내면서 다른거 밀기 popleft하고 append
3. k를 뽑아서 맨 왼쪽 pop하고 appendleft
근데 문제를 읽어보니까 그걸 하고 있으란 얘기가 아니고
하라는대로 하기 위해서 2번, 3번을 몇번이나 해야하나에 대한 결과를 출력(최소)
데이터는 순서대로 밀거나 당기거나니까 그거 숫자로 계산해서 계산하면 훨씬 빨리 풀 수 있겠지
근데 시간이 2초나 되니까 그냥 데크 만들어서 해도 크게 문제 없을 듯
일단 시키는대로 짜보기
index 찾는 원소 위치 체크
len 데크 길이 체크
rotate(n) n 단계 회전 양수 오른쪽 음수 왼쪽'''

'''from collections import deque

n, m = map(int, input().split())
o = list(map(int, input().split()))
q = deque([i+1 for i in range(n)])
ans = 0
for i in range(m):
    t = q.index(o[i])
    if t < len(q)/2:
        ans += t
        q.rotate(-t)
        q.popleft()
    else:
        ans += len(q) - t
        q.rotate(len(q) - t)
        q.popleft()
print(ans)'''

n, m = map(int, input().split())
o = list(map(int, input().split()))
q = [i+1 for i in range(n)]
ans = 0
compensation = 0
for i in range(m):
    t = q.index(o[i])
    if t + compensation < len(q)/2:
        ans += t + compensation
        compensation -= t + compensation
    else:
        ans += len(q) - (t + compensation)
        compensation += len(q) - (t + compensation) - 1
    q.pop(t)
print(ans)
# 회전시키지 않고도 회전시킨만큼을 보정해줄 수 있는 방법이 필요하다
# ans += target_index가 맞다