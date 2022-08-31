'''
6%, 시간 초과
'''
import sys
ssr = sys.stdin.readline

def check_city_num(start, end):
    if start == end:
        city_table[start] += 1
    else:
        for i in range(start, end + 1):
            city_table[i] += 1 # 이렇게 한다음에 나중에 구간별로 제일 작게 나온 놈 선택해 나갈까

def select_city(start, end):
    global cnt
    tmp = city_table.index(min(city_table[start:end+1]), start, end+1)#이게 O(n)짜리다
    if city_table[tmp] == 0 or city_table[tmp] == 10**5+1:
        return
    else:
        city_table[tmp] = 10**5+1
        cnt += 1
    
t = int(ssr())
for _ in range(t):
    m,n = map(int, ssr().split())
    city_table = [0 for _ in range(m)]
    section = []
    for _ in range(n):
        tmp = list(map(int, ssr().split()))
        if tmp[0] > tmp[1]:
            section.append([tmp[0], m-1])
            section.append([0, tmp[1]])
        else:
            section.append(tmp)
    # section = [list(map(int, ssr().split())) for _ in range(n)]
    if n < m :
        print('NO')
        continue
    cnt = 0
    for i in section:
        check_city_num(i[0], i[1])
    for i in section:
        select_city(i[0], i[1])
    if cnt == m:
        print('YES')
    else:
        print('NO')
'''
그래프
그리디

모든 도시를 다 선택하진 않아도 상관없나?
그냥 몇 개 덜 선택되더라도 중복만 안되면 상관없는건가
m-1 ~ 0은 처음부터 끝까지가 아니라 링월드의 구조상 맨 마지막 도시와 시작 도시가 붙어있고 그 두 개의 경로를 말한다
아마 입력의 특징상 거꾸로된 경로는 나오지 않을 가능성이 크다
참았다가 내일 하자 22일에
'''