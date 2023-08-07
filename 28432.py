'''
중복되는 단어는 안됨, 후보로는 들어올 수 있음
앞 단어의 마지막 글자를 첫번째로, 뒷글자의 첫번째 글자를 마지막으로
? = previous_word[-1] + ... + next_word[0]

?는 첫번째나 마지막에도 올 수 있음
첫번째면 이전 단어가 없고 마지막이면 이후 단어가 없다

아예 입력이 ?만 있을 수 있겠네
'''

import sys
ssr = sys.stdin.readline

n = int(ssr())
s = []
loc = 0 
for i in range(n):
    word = ssr().rstrip()
    s.append(word)
    if word == '?':
        loc = i
m = int(ssr())
first, last = '', ''
a = ''
if n == 1:
    print(ssr().rstrip())
else:
    for _ in range(m):
        nomi = ssr().rstrip()
        if not nomi in s:
            if loc == 0:
                last = s[loc+1][0]
                if nomi[-1] == last:
                    a = nomi
            elif loc == n-1:
                first = s[loc-1][-1]
                if nomi[0] == first:
                    a = nomi
            else:
                first = s[loc-1][-1]
                last = s[loc+1][0]
                if nomi[0] == first and nomi[-1] == last:
                    a = nomi
    print(a)