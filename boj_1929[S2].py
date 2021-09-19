def check_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return n

M,N = map(int,input().split())
num_list = [x for x in range(M,N+1)]
check_list = []
for i in range(len(num_list)):
    out = check_prime_number(num_list[i])
    if type(out) == int:
        check_list.append(out)
for i in check_list:
    print(i)