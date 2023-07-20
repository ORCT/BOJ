'''
1. 단어의 첫글자가 단축키로 지정되었는지 확인
2. 첫글자로 단축키 지정을 못하면 왼쪽부터 다시 한글자씩 확인
3. 그래도 못하면 그냥 놔두는데 전부 소문자로 변경
4. 모든 입력에 대해 적용
'''

import sys
ssr = sys.stdin.readline

def query1(words):
    for i in range(len(words)):
        words[i] = list(words[i])
        if words[i][0] not in hotkeys:
            hotkeys[words[i][0].lower()] = 0
            hotkeys[words[i][0].upper()] = 0
            words[i][0] = '[' + words[i][0] + ']'
            words[i] = ''.join(words[i])
            print(' '.join(words))
            return True
        words[i] = ''.join(words[i])
    else:
        return False

def query2(words):
    for i in range(len(words)):
        words[i] = list(words[i])
        for j in range(len(words[i])):
            if words[i][j] not in hotkeys:
                hotkeys[words[i][j].lower()] = 0
                hotkeys[words[i][j].upper()] = 0
                words[i][j] = '[' + words[i][j] + ']'
                words[i] = ''.join(words[i])
                print(' '.join(words))
                return True
        words[i] = ''.join(words[i])
    else:
        print(' '.join(words))

n = int(ssr())
hotkeys = {}
for _ in range(n):
    words = ssr().rstrip().split()
    if not query1(words):
        query2(words)