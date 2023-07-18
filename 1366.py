'''
모든 줄은 코드에 있는 음 중 하나를 꼭 내야 한다.
그 중에 이제 프렛을 안눌러도 되는 놈이 있는 거고 눌러야만 되는 놈이 있는거
눌렀다면 누른 놈들끼리 싹 모아서 그 중에 제일 높은 번호를 누른 놈과 제일 낮은 번호를 누른 놈의 차에 1을 더한다
그게 출력값

만약 줄이 두개인데 하나는 누르고 하나는 안누르면
누른거에서 안누른거를 빼는게 아니라 누른거 빼기 누른거 해서 난이도가 1되는건가?
전부 안눌러야만 그럼 0이 되겠네

예제 4번의 함정에 빠지지마라 문제가 잘못된 것이 아니다
난이도가 6을 넘어간다면 차라리 낮은 프렛보다 아예 높은 프렛을 이용해서(12프렛을 이동하면 된다) 좀 더 가까이 붙일 수 있다

눌러야 하는게 3개라고 치자 1 8 9 이라고 해보자고
원래는 9 - 1 + 1 해서 9인데 1을 13프렛으로 이동시키면
8 9 13 해서 13 - 8 + 1 해서 6으로 만들 수 있어 이걸 또 하면?
9 13 20 해서 12 다시
1 6 11
11 - 1 + 1 = 11
13 - 6 + 1 = 8
19 - 11 + 1 = 9
'''

def f(string_idx, result):
    if len(result) == n:
        for i in visited:
            if i == 0:
                return
        else:
            if max(result) == 0 and min(result) == 0:
                ans.append(0)
            else:
                sorted_result = sorted(result)
                tmp = []
                max_result = sorted_result[-1]
                min_result = 0
                for i in sorted_result:
                    if i != 0:
                        min_result = i
                        tmp.append(max_result - min_result)
                        break
                for i in range(1, len(sorted_result)):
                    if sorted_result[i-1] != 0:
                        tmp.append(sorted_result[i-1] + 12 - sorted_result[i])
                ans.append(min(tmp) + 1)
    else:
        for j in range(m):
            visited[j] += 1
            result.append(frets[string_idx][j])
            f(string_idx+1, result)
            visited[j] -= 1
            result.pop()
            
n, m = map(int, input().split())
strings = input().split()
chords = input().split()
notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
frets = [[] for _ in range(n)]
for i in range(n):
    for j in chords:
        frets[i].append((notes[j]-notes[strings[i]]+12)%12)
ans = []
visited = [0 for _ in range(m)]
f(0, [])
print(min(ans))