def check_prime_num(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            if i == n-1:
                return n
            else:
                continue

N = int(input())
num_list = list(map(int, input().split()))
check_list = []
for i in range(len(num_list)):
    if num_list[i]==2:
        check_list.append(num_list[i])
    out = check_prime_num(num_list[i])
    if type(out) == int:
        check_list.append(out)
print(len(check_list))