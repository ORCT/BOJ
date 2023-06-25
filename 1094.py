x = int(input())
w = [64, 32, 16, 8, 4, 2, 1]
c = 0
cnt = 0
for i in range(len(w)):
    if w[i] > x:
        continue
    elif w[i] == x:
        print(1)
        break
    else:
        if c + w[i] <= x:
            c += w[i]
            cnt += 1
            if x == c:
                print(cnt)
                break
'''
막대를 몇 번 자르냐가 아니라 막대를 몇 개 붙일거냐고~'''