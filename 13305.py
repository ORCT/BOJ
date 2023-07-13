'''
도로의 길이와 기름 노드의 번호가 가격으로 주어지는 그래프
1km에 1L를 사용
도로는 다행히도 전부 직선상에 존재

어차피 맨왼쪽에서 맨오른쪽에 도착하면 끝나는 문제
싼곳에 도착하기 전에는 현재의 가격보다 싼 곳에 도착할 때 까지의 최소한만 넣는거임

문제를 기준으로 보면
처음에 5고 2까지의 거리가 2니까
2리터만 넣어/10원
2다음은 4니까 스킵하고 1에 도착할 때까지가 4니까 4를 넣어
10 + 8해서 18원

일반화하면 '현재의 가격보다 (가장 가까운)싼 곳에 도착하기 위해 필요한 최소한을 넣는다'

마지막까지 갔는데 현재보다 싼 곳이 없을 경우
'''

# def f(current, money):
#     for i in range(current, len(p)):
#         if p[i] < p[current]:
#             money += sum(l[current:i]) * p[current]
#             money = f(i, money)
#             return money
#     else:
#         money += sum(l[current:]) * p[current]
#     return money

# n = int(input())
# l = list(map(int, input().split()))
# p = list(map(int, input().split()))
# print(f(0, 0))


# def f(current, money):
#     if (current, money) in memo:
#         return memo[(current, money)]

#     for i in range(current, len(p)-1):  # 마지막 요소를 제외
#         if p[i] < p[current]:
#             money += sum(l[current:i]) * p[current]
#             money = f(i, money)
#             memo[(current, money)] = money
#             return money
#     else:
#         money += sum(l[current:]) * p[current]
    
#     memo[(current, money)] = money
#     return money

# memo = {}
# n = int(input())
# l = list(map(int, input().split()))
# p = list(map(int, input().split()))
# print(f(0, 0))

n = int(input())
l = list(map(int, input().split()))
p = list(map(int, input().split()))
min_p = p[0]
ans = 0
for i in range(1, len(p)):
    ans += l[i-1] * min_p
    if p[i] < min_p:
        min_p = p[i]
print(ans)