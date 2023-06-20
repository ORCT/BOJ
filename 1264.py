'''
1. brute force
'''

while True:
    s = input()
    cnt = 0
    if s == '#':
        break
    else:
        for i in s.lower():
            if i in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        print(cnt)