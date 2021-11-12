n = int(input())
num = 1
cnt = 0
while 1:
    if str(num).find('666') != -1:
        cnt += 1
        if n == cnt:
            print(num)
            break
    num += 1