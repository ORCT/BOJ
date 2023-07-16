'''
사람들은 자기보다 큰 사람이 왼쪽에 몇명있었는지만을 기억한다.
키는 1~N
2초, 20억회

둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 **키가 큰 사람이 왼쪽에 몇명** 있는지가 주어짐

줄을 선 순서대로 키를 출력한다.

순서가 왔다갔다 하니까 헷갈리는 거에 주의

0번째 숫자는 키가 1인 사람(가장 작은 사람)의 위치를 나타낸다. 즉 이걸 기준으로 생각할 수 있다.

n이 10이하니까 백트래킹/브루트 포스 할 수 있지 않을까

1. 일단 1자리 고정
2. n-1를 빈 칸 중 제일 앞에 넣어봄(근데 n은 어디에 있든지 0이라서 n은 그냥 남는 자리에 넣는거로 하고)
3. line에서 n-1 앞에 몇 개가 있어야 하는지 확인
3-1. 조건에 맞으면 n-2로 넘어가서 반복
3-2. 조건에 안맞으면 다시 2로 가서 n-1을 한칸 뒤로 밈

해결할 것 : 조건에 맞는지 안맞는지 판단 어떻게 해? 
한 번 옮길 때 마다 앞에 i 보다 큰게 있는지 i 위치 까지 이동하면서 갯수 셀까 나쁘지 않은 듯


'''

'''def f(person, start): #7 #6
    if person == 1:
        return
    for i in range(start, n+1):
        if ans[i] == 0:
            case = check(person, line[person-1], i)
            if case == 0: # 맞으면 뒤에 숫자로 시작하는 재귀로 짜면 될 듯
                if visited[person] == False:
                    ans[i] = person # 0 7 6 0 0 0 0 1
                    visited[person] = True
                f(person-1, 1) # 어 이게 아니네 하고 recur depth가 하나 올라왔을 때 어떻게 해야할까
                # ans[i] = 0
            elif case == 1:
                # ans[i] = 0
                continue
            else:
                ans[ans.index(person+1)] = 0
                return

def check(num, tall_num, loc_cur): # 7 0 1
    cnt = 0
    for i in range(loc_cur):
        if ans[i] > num:
            cnt += 1
    if cnt == tall_num:
        return 0
    elif cnt < tall_num:
        return 1
    else:
        return 2
        
n = int(input())
line = list(map(int, input().split()))
visited = [False for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
ans[line[0]+1] = 1
f(n, 1)
print(*ans[1:])'''

# 0 0 0 0 0 0 0 1
# 7을 썼을 때 0 7 0 0 0 0 0 1
# 6을 썼을 때

# 잘못 집어넣은 위치에서 체크 돌려서 cnt 봤을 때 작은 경우가 있고 큰 경우가 있을 수 있음
# 작은 경우 continue 해서 개수 맞아질 때 까지 뒤로 위치를 밀면 돼
# 큰 경우(예를 들어서 line에서는 0이랬는데 실제로 넣어보니까 1인 경우)
# 앞의 숫자가 잘못 된거니까 지금 사람 보다 더 앞으로 돌아가야함

n = int(input())
line = list(map(int, input().split()))
ans = [0 for _ in range(n)]
for i in range(len(line)): # 현재 선택된 친구
    cnt = 0
    for j in range(len(line)): # 바꿔가면서 비교중인 자리
        if ans[j] == 0 and cnt == line[i]:
            ans[j] = i+1
            break
        elif ans[j] > i+1 or ans[j] == 0:
            cnt += 1
print(*ans)