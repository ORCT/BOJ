'''
제발 알고리즘 분류 좀 먼저 보지마

일반 dp -> 메모리 초과 = 배열 만들어서 값 전부 담지마
계산하면서 미리 mod해도 안돼~

계산은 뭐 그냥 이대로 하되 메모리 오버만 안나면 되는건가

메모리 오버가 나는데 피보나치를 구하라고 한다? = 뭔가 순환하는게 있어서 메모리가 클 필요가 없다

피사노 주기

생각보다 여러가지 풀이들이 있는 것 같다.
피사노주기, 점화식 전개를 통한 규칙 파악, 행렬의 거듭제곱

피사노 주기 : 피보나치수를 임의의 수 k로 나눌 때 나머지는 수열은 주기를 갖는다. 이 주기를 피사노 주기라고 한다.
반복문을 통해서 주기를 구하는 방법도 있을 것이고, n번째 수를 k로 나누는 것을 통해서 주기가 어떻게 나오는지 식으로도 밝힐 수 있을 것이다.
근데 이거는 피사노 주기로 풀기에도 입력이 큼

그래서 분할정복을 이용한 제곱
'''
# n = int(input())
# fb = [0 for _ in range(n+1)]
# fb[1] = 1
# for i in range(2, n+1):
#     fb[i] = (fb[i-1] + fb[i-2])%1000000007
# print(fb[n])

# import sys
# sys.setrecursionlimit(1000000000)

# def recur(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return recur(x-1) + recur(x-2)

# n = int(input())
# print(recur(n)%1000000007)

def matrix_multiplication(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
            result[i][j] %= 1000000007
    return result
            
n = int(input())
ans = [[1, 0], [0, 1]]
fib_mat = [[1, 1], [1, 0]]
while n > 0:
    if n%2 == 1:
        ans = matrix_multiplication(ans, fib_mat)
    fib_mat = matrix_multiplication(fib_mat, fib_mat)
    n //= 2
print(ans[1][0])