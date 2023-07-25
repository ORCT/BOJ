'''
지민이가 거짓말쟁이가 되지 않는 방법
지민이는 모든 파티에 참여해야한다.
진실을 아는 사람 앞에서는 사실만 말해야한다

이미 진실을 들은 사람에게는 진실만을
이미 거짓을 들은 사람에게는 거짓만을

즉 진실을 아는 사람과 한 번이라도 같은 파티에 참석하는 사람들에게는 거짓을 말할 수 없다

knowing_truth에 값을 추가하고 다 체크하려고 했는데 그냥 사람 번호만큼 배열 만들고
그 값이 1이면 진실을 아는 사람, 0이면 모르는 사람해서 인덱스로 호출해보면 O(1)로 체크 가능하지 않나

지민이가 사람들의 스케줄을 전부 체크한 후에 거짓말을 할 수 있겠다는 생각이 드는 파티의 수를 결과로 출력한다.
미리 체크가 가능해야한다
하면서 체크할 경우 사실은 거짓말을 하면 안되는 파티가 포함이 안될 수 있다

반례:
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
>> 0

순서대로만 집어넣는 건 약간 위험하겠다.
진실을 표기할 때 마다 반복문을 돌도록 해야하나
파티 목록도 방문처리를 하면 이미 체크한 목록은 안돌아도 되려나?(어차피 사람을 진실 표시를 하면 자동으로 이미 체크한 파티는 안돌듯)

bfs처럼 해서 queue 안에 있는 인자를 빼가지고 파티 목록을 돌도록 하면?
'''

from collections import deque
import sys
ssr = sys.stdin.readline

def check_truth():
    while q:
        p = q.popleft()
        for party in parties:
            if p in party[1:]:
                for i in party[1:]:
                    if visited[i] == False:
                        q.append(i)
                        visited[i] = True
    
n, m = map(int, ssr().split())
knowing_truth = list(map(int, ssr().split())) # 0 : num of person, 1~ : person's num
visited = [False for _ in range(n+1)]
q = deque([])
for i in knowing_truth[1:]:
    visited[i] = 1
    q.append(i)
parties = [list(map(int, ssr().split())) for _ in range(m)]
check_truth()
for party in parties:
    for i in party[1:]:
        if visited[i] == 1:
            m -= 1
            break
print(m)