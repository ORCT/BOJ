def check_prime_number(n):
    if n == 2:
        return n
    for i in range(2,n):
        if n%i==0:
            break
        else:
            if i == n-1:
                return n
            else:
                continue

M = int(input())
N = int(input())
num_list = [x for x in range(M,N+1)]
check_list = []
for i in range(len(num_list)):
    out = check_prime_number(num_list[i])
    if type(out) == int:
        check_list.append(out)
if len(check_list)==0:
    print(-1)
else:
    print(sum(check_list))
    print(check_list[0])