N,M = map(int, input().split())
cards = list(map(int, input().split()))
check_num = 0
for i in range(len(cards)):
    a = cards[i]
    for j in range(i+1,len(cards)):
        b = cards[j]
        for k in range(j+1, len(cards)):
            c = cards[k]
            if check_num <= a+b+c and a+b+c<=M:
                check_num = a+b+c
                #print('{}+{}+{}='.format(a,b,c),check_num)
print(check_num)