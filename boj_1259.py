import sys
ssr = sys.stdin.readline

while 1:
    num = ssr().rstrip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    elif num != num[::-1]:
        print('no')