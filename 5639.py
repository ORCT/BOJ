'''
일단 이진 탐색 트리임 왼쪽은 부모보다 작고 오른쪽은 부모보다 큼
근데 서브 트리도 그걸 모두 만족해야함, 예를 들어서 루트 노드의 오른쪽에 서브트리가 있다고 쳤을 때
오른쪽에 있는 서브 트리는 루트 노드보다 무조건 다 커야함
서브 트리에 있는 특정 부모 노드보다 작은 값(왼쪽)이라고 하더라도 루트보다 커야함
트리는 안주어지고
전위 순회한 결과를 주고 그걸로 트리를 유추하고
후위 순회 했을 때의 결과를 출력

전위 순회:
재귀로 하는 dfs랑 방문순서 같음

후위 순회 : 더 이상 안 간 자식 노드가 없을 때 까지 자식 노드를 돌고 부모노드 출력
1
2 3
이 있으면 2 3 1의 방문순서

전위 순회 결과로 트리 알아내려면
일단 지금 값이랑 다음 값 비교
더 작으면 왼쪽 크면 오른쪽

1. 처음 값이 루트
2. 처음값이랑 비교해서 작으면 왼쪽, 왼쪽거 저장
3. 그거보다 작으면 또 왼쪽, 또 저장
4. 그거보다 작으면 또 왼쪽, 또 저장
5. 지금 값 보다 큼 위로 올라가
6. 또 큼, 근데 부모 보다는 안큼, 그럼 왼쪽
.
.
.
뭐 이런식으로 다음 값을 가지고 이전 값, 현재 값이랑 비교해가면서 트리를 연결하면 될 듯
근데 노드에 들어있는 값이 10^6이라 이걸 그대로 노드 번호로 쓸 수는 없고
각 값에 노드 번호를 부여하는 방법을 쓰면 좀 편하게 하려나, 그래도 최대 10000개까지는 이름 붙여야 함

이게 딕셔너리 만들어도 자기 부모를 키로 가지는게 탐색하기 편할거 같은데

바로 직전 값이 내 부모가 아닐 경우에 타고 올라가기 좀 편해야 하는데

맨 위까지 다시 올라왔는데도 루트보다 크면 어쩔래
그냥 오른쪽에 저장해야하는데
일반 조건문으로 일단 짜볼까

오른 쪽에 저장된 애
트리를 자식을 값으로 가지는거랑 부모를 값으로 가지는거 2개를 만들어야겠어

방금 입력된 값이 부모보다 크면 타고 올라가는데, 그 타고 올라가는 경로를 좀 저장해두면 어떨까

반례
50
30
24
5
27
25
26
28
29
45
98
52
60
106
109
108
110
>>
5
26
25
29
28
27
24
45
30
60
52
108
110
109
106
98
50

이거는 거꾸로 탈게 아니라 매 원소를 추가할 때 마다 루트 노드부터 타는게 맞겠다.

'''

'''
import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(100000)

def make_tree():
    first_key = int(ssr())
    tree = {first_key:[0, 0]}
    while True:
        try:
            cur_key = int(ssr())
            tree[cur_key] = [0, 0]
            parent_key = first_key
            while True:
                if cur_key < parent_key: # 부모보다 작으면
                    if tree[parent_key][0] == 0: # 왼쪽 비어있으면
                        tree[parent_key][0] = cur_key
                        break
                    else: # 왼쪽 안 비어 있으면
                        parent_key = tree[parent_key][0] # 키 왼쪽 아래로 이동
                else: # 부모보다 크면
                    if tree[parent_key][1] == 0: # 오른쪽 비어 있으면
                        tree[parent_key][1] = cur_key
                        break
                    else: # 오른쪽 안 비어있으면
                        parent_key = tree[parent_key][1] # 오른쪽 아래로 이동
        except:
            return first_key, tree

def postorder(n):
    if n == 0:
        return
    else:
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n)
        return
    
start, tree = make_tree()
postorder(start)
'''

'''
import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10000)

def postorder(tree):
    if len(tree) == 0:
        return
    else:
        parent = tree[0]
        left = []
        right = []
        for i in range(1, len(tree)):
            if parent > tree[i]:
                left.append(tree[i])
            else:
                right.append(tree[i])
        postorder(left)
        postorder(right)
        print(parent)
        
nodes = []
while True:
    try:
        nodes.append(int(ssr()))
    except:
        break
postorder(nodes)
'''

import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10002)

def postorder(start, end):
    if start >= end:
        return
    mid = start+1
    for i in range(start+1, end):
        if preorder[start] < preorder[i]:
            mid = i
            break
    postorder(start+1, mid)
    postorder(mid, end)
    print(preorder[start])
        
preorder = []
while True:
    try:
        preorder.append(int(ssr()))          
    except:
        break
postorder(0, len(preorder))