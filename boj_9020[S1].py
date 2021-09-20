import sys
def check_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return n

T = int(input())
for i in range(T):
    n = int(sys.stdin.readline())
    check = 0
    for i in range(int(n/2)+1):
        a = check_prime_number(i)
        b = n-a
        if b == check_prime_number(b):
            check = a
    print(check, n-check)