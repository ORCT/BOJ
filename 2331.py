a,p = input().split()
n = [a]
num = {i:0 for i in range(1,236197)}
num[int(a)] = 1
tmp = 0
while 1:
    c = n[-1]
    for i in c:
        tmp += int(i)**int(p)
    n.append(str(tmp))
    if num[tmp] == 1:
        print(len(n[:n.index(str(tmp))]))
        break
    else:
        num[tmp] += 1
        tmp = 0
    
#236,196 : max