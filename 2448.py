'''
n이 높이랑 같네

작은 삼각형이 다음 숫자에서 좌우로 빠지는 모양같음

아니면 5*3을 기준으로 처음에는 가운데 빼고 비우고
두번째는 가운데 양 옆 빼고 비우고
세번째는 다 채우고
'''

def recur(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    else:
        half = n//2
        before = recur(half)
        result = ['' for _ in range(n)]
        for i in range(half):
            result[i] = ' '*(half) + before[i] + ' '*(half)
        for i in range(half, n):
            result[i] = before[i-half] + ' ' + before[i-half]
        return result

n = int(input())
ans = recur(n)
for i in ans:
    print(i)