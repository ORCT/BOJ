from string import ascii_uppercase
import sys
ssr = sys.stdin.readline

def preorder(v):
    global ans
    if visited[v] == 1:
        return
    visited[v] = 1
    ans += str(v)
    for i in edges:
        if i[0] == v:
            for j in range(1,3):
                if i[j] != '.':
                    preorder(i[j])

def inorder(v):
    global ans
    if visited[v] == 2:
        return
    visited[v] = 2
    for i in edges:
        if i[0] == v:
            if i[1] != '.':
                inorder(i[1])
            ans += i[0]
            if i[2] != '.':
                inorder(i[2])
            
def postorder(v):
    global ans
    if visited[v] == 3:
        return
    visited[v] = 3
    for i in edges:
        if i[0] == v:
            for j in range(1,3):
                if i[j] != '.':
                    postorder(i[j])
            ans += i[0]
                    
n = int(ssr())
edges = [ssr().rstrip().split() for _ in range(n)]
visited = {i:0 for i in ascii_uppercase}
ans = ''

preorder('A')
print(ans)
ans = ''

inorder('A')
print(ans)
ans = ''

postorder('A')
print(ans)
ans = ''