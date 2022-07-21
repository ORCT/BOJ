n = int(input())
line_len = 4*(n-1)+1
cnt = 1
stars = [['*' for _ in range(line_len)] for _ in range(line_len)]
while line_len - 2*cnt >= 1:
    for i in range(cnt, line_len-cnt):
        for j in range(cnt, line_len-cnt):
            if cnt%2 == 1:
                stars[i][j] = ' '
            else:
                stars[i][j] = '*'
    cnt += 1
for i in stars:
    print(''.join(i))

'''
1 = 1
2 = 5
3 = 9
4 = 13
꽉 채운 다음에 한칸 안으로 밀고 비우고, 한칸 안으로 밀고 다시 채우고는 어때
'''
'''def sol(num):
    global cnt
    if num == 0:
        return
    for i in range(cnt,):
        for j in range():
            stars[i][j] = '*'
    for i in range():
        for j in range():
            stars[i][j] = ' '
    return sol(num-1)

n = int(input())
line_len = 4*(n-1)+1
cnt = 1
stars = [['*' for _ in range(line_len)] for _ in range(line_len)]
while line_len - 2*cnt >= 1:
    for i in range(cnt, line_len-cnt):
        for j in range(cnt, line_len-cnt):
            if cnt%2 == 1:
                stars[i][j] = ' '
            else:
                stars[i][j] = '*'
    cnt += 1
for i in stars:
    print(''.join(i))'''