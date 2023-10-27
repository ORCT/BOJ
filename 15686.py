'''
0 빈칸
1 집
2 치킨집

거리는 수직거리 수평거리 합

m개의 치킨집만 남겨두고 전부 폐업시킬 때 도시의 치킨 거리가 가장 작게 될지 구하는 것이 목표

치킨 거리 = 집에서 가장 가까운 치킨집까지의 거리
총 치킨 집의 갯수만큼 각각 집까지의 거리를 구해야함
칸 당 1의 거리를 가지니까 치킨집이랑 그냥 집의 좌표를 저장해서 각자 산술로 구할 수 있을거 같은데

근데 집 당 치킨 거리를 구해봤자 어떤 치킨집을 없애버리는게 좋은지 직관적으로 알수는 없어
집 당 치킨거리는 그냥 도시 치킨거리 구하는 재료로만 쓰일 뿐
그럼 어떤 치킨집을 폐업시키는게 좋은지는 어떻게 알지?
모든 집까지의 치킨 거리를 구한 다음에 그 합이 가장 큰 놈들부터 죽이는 건 어때?
그게 정해인지 증명할 방법이 있나?

특정 치킨집에서 모든 집까지의 거리의 합을 구한 다음에 그 값이 큰 애들을 날리면
그게 치킨거리의 전체적인 하락으로 이어지지 않을까

모든 치킨 집의 조합에 대해서 도시치킨거리를 계산해서 최솟값 출력
브루트포스

최대 13Cm의 조합에 치킨집당 100번 이니까 연산량이 100m*13Cm 정도?
'''
import sys; ssr = sys.stdin.readline
INF = 2501

def get_chicken_distance(chicken_locations, house_locations):
    result = []
    for house_r, house_c in house_locations:
        chicken_distance = INF
        for chick_r, chick_c in chicken_locations:
            tmp = abs(chick_r - house_r) + abs(chick_c - house_c)
            if tmp < chicken_distance:
                chicken_distance = tmp
        result.append(chicken_distance)
    return result

def f(num, idx, selected_chickens):
    global ans
    if num == m:
        tmp = sum(get_chicken_distance(selected_chickens, houses))
        if tmp < ans:
            ans = tmp
        return
    for i in range(idx, len(chickens)):
        selected_chickens.append(chickens[i])
        f(num+1, i+1, selected_chickens)
        selected_chickens.pop()
        
n, m = map(int, ssr().split())
city = [list(map(int, ssr().split())) for _ in range(n)]
houses = []
chickens = []
dists = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))
ans = INF
f(0, 0, [])
print(ans)