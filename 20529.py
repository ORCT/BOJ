'''
브루트포스
가장 가까운 3명을 고를것
어차피 같은지 안같은지를 구분할거라면 받을 때 부터 istj랑 비교해서 다른만큼 점수를 부여하면 어때
어차피 점수는 그냥 서로가 다른거의 갯수만큼 1을 더하니까
상관없을 거 같은데

3명 이상이 주어질 때 어떻게 사람들을 고를 것인가
또 백트래킹 써야해?

N의 범위가 커서 실제로 하나씩 조합해보는 경우에는 시간초과에 걸릴 수 있다
비둘기집의 원리를 찾아봐라

비둘기집 원리 : n+1개의 물건을 n개의 상자에 넣을 때 적어도 한 상자에는 두 개 이상의 물건이 들어있다는 원리
그러면 이걸 어떻게 이 문제에 적용해볼 수 있을까
모든 mbti가 중복없이 들어온다는 가정을 세웠을 때 mbti는 총 16개이므로 n이 17이라면 최소한 하나의 mbti는 중복된다고 볼 수 있다.
이것을 확장해서 3명의 심리적 거리를 구하는 문제이므로,
같은 mbti가 총 3개 있다면 해당 케이스의 최소거리는 0이다.
여기에 비둘기집의 원리를 접목했을 때
n이 33이상이면 최소한 같은 mbti를 가진 사람이 3명은 존재한다는 뜻이고 이 경우 최소거리는 0이 된다.
따라서 n이 33보다 큰 경우는 그냥 0을 출력하도록 코드를 수정한다.
'''

import sys
ssr = sys.stdin.readline

def cal_dist(stu_stack):
    result = 0
    for i in range(2, -1, -1):
        for j in range(4):
            tmp = 0
            if stu_stack[i][j] != stu_stack[i-1][j]:
                tmp += 1
            result += tmp
    return result

def f(start, stu_stack):
    if len(stu_stack) == 3:
        distance = cal_dist(stu_stack)
        ans.append(distance)
        return
    for i in range(start, n):
        if visited[i] == False:
            visited[i] = True
            stu_stack.append(students[i])
            f(i+1, stu_stack)
            visited[i] = False
            stu_stack.pop()

t = int(ssr())
for _ in range(t):
    n = int(ssr())
    students = ssr().strip().split()
    if n > 32:
        print(0)
    else:
        visited = [False for _ in range(n)]
        ans = []
        f(0, [])
        print(min(ans))