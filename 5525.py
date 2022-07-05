'''n = int(input())
m = int(input())
s = input()
p = 'I'+'OI'*n
ans = 0
for i in range(m-len(p)):
    if s[i] == 'I':
        num = 0
        for j in range(len(p)):
            if s[i+j] == p[j]:
                num += 1
            else:
                break
        if num == len(p):
            ans += 1
print(ans)'''
'''n = int(input())
m = int(input())
s = input()
p = 'I'+'OI'*n
ans = 0
for i in range(m-len(p)):
    if s[i] == 'I':
        if s[i:i+2*n+1] == p:
            ans += 1
print(ans)'''

def check():
    global state, start
    cnt = 0
    while start < m:
        if state == 1:
            if s[start] == 'I':
                state = 0
                start += 1
                cnt += 1
            else:
                start += 1
                return cnt
        else:
            if s[start] == 'O':
                state = 1
                start += 1
            else:
                state = 1
                return cnt
    return cnt

n = int(input())
m = int(input())
s = input()
state = 1
ans = 0
start = 0
while start < m:
    cnt = check()
    if cnt - n < 0:
        ans += 0
    else:
        ans += cnt - n
print(ans)