'''
문자열 길이가 한번에 하나만 딱 바뀐다고 가정하면
1000000*36이 얼추 5번 정도 가능하니까
지금 이거보다 좀 더 연산량을 줄여야 함

어제 풀었던거처럼 비슷하게 해서 보낼라면 할수도 있을 거 같긴 한데'''

'''
import sys
sys.setrecursionlimit(1e6+1)

def f(start, end, strings):
    restart = start
    while start < end:
        for i in range(start, end):
            if s[i] == e[0]:
                substrings, restart = f(i+1, end, e[0])
                strings += substrings
                start = restart
                break
            elif s[i] == e[-1]:
                if strings+s[i] == e:
                    return '', i+1
                else:
                    strings += s[i]
                    start = i+1
            else:
                strings += s[i]
                start = i+1
    return strings, end
            
s = input()
e = input()
ans, _ = f(0, len(s), '')
print(ans if ans != '' else 'FRULA')
'''

s = input()
e = input()
stack = []
for char in s:
    stack.append(char)
    if char == e[-1]:
        if ''.join(stack[-len(e):]) == e:
            for _ in range(len(e)):
                stack.pop()
ans = ''.join(stack)
print(ans if ans != '' else 'FRULA')