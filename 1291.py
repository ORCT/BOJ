'''
이면수
어비스 오엘 우테(2, 3, 4의 합으로 만들 수 있는 수 = 1이랑 5이외의 모든 수)에 속해있어야하고, 
    자릿수의 합이 홀수

임현수
chicken number(4) 혹은 starcraft number(2),
합성수(1이랑 자기 자신 빼고 약수 있는거)이면서, 
    소인수(약수가 소수인거)의 종류의 개수가 짝수개

성경수
위의 두개가 아닌거'''

n = int(input())
ans = []

def factorization(num, prime_factors):
    if num == 1:
        return prime_factors
    for i in range(2, num+1):
        if num % i == 0:
            factorization(num//i, prime_factors)
            prime_factors.append(i)
            return prime_factors

def one(n):
    if n == 4 or n >= 6:
        s = sum([int(i) for i in str(n)])
        if s % 2 == 1:
            return True
        else:
            return False
    else:
        return False
        
def two(n):
    if n == 2 or n == 4:
        return True
    else:
        prime_factors = factorization(n, [])
        prime_factors = set(prime_factors)
        if len(prime_factors) != 0 and len(prime_factors) % 2 == 0:
            return True
        else:
            return False
        
ans.append(one(n))
ans.append(two(n))
if ans[0] == True:
    if ans[1] == True:
        print(4)
    else:
        print(1)
else:
    if ans[1] == True:
        print(2)
    else:
        print(3)