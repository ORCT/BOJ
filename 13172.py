'''
어떤 수 a = p * q 일 때,
어떤 정수 p에 대해 p * q equiv 1(mod x) 라면
q는 p의 모듈러 역원이라고 한다.
표기는 p^(-1)로 한다

여기서의 기댓값 = 분수들의 합
모듈러 연산의 덧셈 법칙
(a + b)mod c = ((a mod c) + (b mod c)) mod c
즉, 입력 받는 대로 전부 mod 하고 다시 다 더해서 mod
그 기댓값을 기약분수로 나타내고 그 기약분수의 형태가 a/b이면
(a * b의 역원)%1000000007 를 구해라'''

import sys
input = sys.stdin.readline
X = 1_000_000_007 # 자릿수 구분할 때 언더스코어를 사용해도 됨

def get_ni(n, x):
    result = 1
    while x > 0:
        if x % 2 == 1:
            result = result * n % X
        n = n * n % X
        x //= 2
    return result

m = int(input())
ans = 0
for _ in range(m):
    n, s = map(int, input().split()) # n이 분모, s가 분자
    # n * ni % 1000000007 = 1 = ((n % 1000000007) * (ni % 1000000007)) % 1000000007
    # 페르마의 소정리에 의해  ni = n^(x-2)%x
    ni = get_ni(n, X-2)
    ans += ni * s % X
print(ans % X)