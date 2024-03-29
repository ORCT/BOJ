import sys
ssr = sys.stdin.readline

t = [[0 for _ in range(101)] for _ in range(101)]
n = int(ssr())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    x,y = map(int, ssr().split())
    ans = 0 
    for i in range(10):
        for j in range(10):
            t[x+i][y+j] = 1
    for i in range(101):
        for j in range(101):
            for k in range(4):
                if t[i][j] == 1 and t[i+dx[k]][j+dy[k]] == 0:
                    ans += 1
print(ans)        


'''
색종이 길이 = 10
색종이가 도화지 밖으로 나가는 경우는 없다
처음에는 그룹 나누기(겹치는 애들은 겹치는 애들끼리)
그룹별 종류 파악(겹치고 내부에 빈 영역, 빈영역x 두가지)
빈영역o : 
근데 이렇게 조건을 나누는 거 보다 n*40에서 겹치는 부분 길이를 빼는게 빠를 거 같기도 하고(어차피 겹치는 부분은 겹치는 애들 전부 다 빼야하니까)
그럼 또 n^2짜리 반복문 돌면서 겹치는 부분 다 찾아야하나
예시 기준: 색종이 4개, 아예 안겹칠 때 : 160, 내부 검은색 일단 무시하면 88
26, 10, 22, 6 : 64 겹치는 길이를 다 빼면 둘레가 나옴
그럼 겹치는 길이를 다 빼는 방법을 구하면 굳이 귀찮게 케이스를 안나눠도 될듯
그럼 처음에 이중반복문 돌 때 겹치는 길이 구한다음에 저장시키면 되겠는데
중복되는 친구들을 처리할 방법이 필요해
5
0 0
10 0
0 10
10 10
5 5
이 경우에 5 5 안에 존재하는 선들은 전부 중복이라 더 빼면 곤란함
특정선이 중복으로 빼졌는지 알 방법이 있을까
모든 선을 시작점과 끝점으로 표현하고 4개의 리스트를 만들어서 진행하면 가능은 할 듯
상당히 귀찮은 작업이 아닌가...
그래서 다들 배열로 풀었나보다
'''