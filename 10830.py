def matmul(mat1, mat2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    return result

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    ans[i][i] = 1
while True:
    if b == 0:
        break
    if b % 2 == 1:
        ans = matmul(a, ans)
    a = matmul(a, a)
    b //= 2
for i in ans:
    print(*i)