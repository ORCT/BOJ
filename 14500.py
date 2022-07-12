import sys
ssr = sys.stdin.readline

def sol1(r,c):#o
    global n,m
    dp = [(0,1),(1,0),(1,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol2(r,c):#i1
    global n,m
    dp = [(0,1),(0,2),(0,3)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol3(r,c):#i2
    global n,m
    dp = [(1,0),(2,0),(3,0)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol4(r,c):#t1
    global n,m
    dp = [(0,-1),(-1,0),(0,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol5(r,c):#t2
    global n,m
    dp = [(-1,0),(0,1),(1,0)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol6(r,c):#t3
    global n,m
    dp = [(0,-1),(1,0),(0,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol7(r,c):#t4
    global n,m
    dp = [(-1,0),(0,-1),(1,0)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol8(r,c):#l1
    global n,m
    dp = [(1,0),(2,0),(2,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol9(r,c):#l2
    global n,m
    dp = [(0,-1),(0,-2),(1,-2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol10(r,c):#l3
    global n,m
    dp = [(-1,0),(-2,0),(-2,-1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol11(r,c):#l4
    global n,m
    dp = [(0,1),(0,2),(-1,2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol12(r,c):#j1
    global n,m
    dp = [(1,0),(2,0),(2,-1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol13(r,c):#j2
    global n,m
    dp = [(0,-1),(0,-2),(-1,-2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol14(r,c):#j3
    global n,m
    dp = [(-1,0),(-2,0),(-2,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol15(r,c):#j4
    global n,m
    dp = [(0,1),(0,2),(1,2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol16(r,c):#s1
    global n,m
    dp = [(0,1),(-1,1),(-1,2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol17(r,c):#s2
    global n,m
    dp = [(1,0),(1,1),(2,1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol18(r,c):#z1
    global n,m
    dp = [(0,1),(1,1),(1,2)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result

def sol19(r,c):#z2
    global n,m
    dp = [(1,0),(1,-1),(2,-1)]
    result = t[r][c]
    for i in dp:
        if 0 <= r+i[0] < n and 0 <= c+i[1] < m:
            result += t[r+i[0]][c+i[1]]
        else:
            return 0
    return result
            
n,m = map(int, ssr().split())
t = [list(map(int, ssr().split())) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        ans.append(sol1(i,j))
        ans.append(sol2(i,j))
        ans.append(sol3(i,j))
        ans.append(sol4(i,j))
        ans.append(sol5(i,j))
        ans.append(sol6(i,j))
        ans.append(sol7(i,j))
        ans.append(sol8(i,j))
        ans.append(sol9(i,j))
        ans.append(sol10(i,j))
        ans.append(sol11(i,j))
        ans.append(sol12(i,j))
        ans.append(sol13(i,j))
        ans.append(sol14(i,j))
        ans.append(sol15(i,j))
        ans.append(sol16(i,j))
        ans.append(sol17(i,j))
        ans.append(sol18(i,j))
        ans.append(sol19(i,j))
print(max(set(ans)))