def people_num(k,n):
    k0 = [i for i in range(1,n+1)]
    for i in range(k):
        for i in range(1,n):
            k0[i] += k0[i-1]
    return k0[-1]

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(people_num(k,n))