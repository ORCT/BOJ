import sys
ssr = sys.stdin.readline

s = ssr().rstrip()
tmp = ''
state = 0
idx = 0
ans = []
for i in range(len(s)):
    if s[i] == '<':
        idx = i
        state = 1
        if tmp != '':
            ans.append(tmp[::-1])
    elif s[i] == '>':
        state = 0
        ans.append(s[idx:i+1])
        tmp = ''
    elif s[i] == ' ' and state != 1:
        ans.append(tmp[::-1]+' ')
        tmp = ''
    else:
        tmp += s[i]
if tmp != '':
    ans.append(tmp[::-1])
print(''.join(ans))