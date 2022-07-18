'''
완전 이진 트리
트리의 높이가 주어진다면 노드의 갯수를 알 수 있다
2^(n+1)-1개의 노드가 존재하고 해당 트리는 오른쪽이 더 작은 수가 위치하므로
해당 성질들을 이용하면 쉽게 풀 수 있으리라 생각된다.
명령에 따라 나오는 갯수를 이용한 식으로 답을 정의할 수 있을 것 같다
바로 앞에 나온 명령이 뭐냐에 따라 빼는 값이 (...RL)*2-1이 될 수도 (...LR)*2+1이 될 수도 있다'''
'''line = input().strip()
if line.isdigit():
    print(2**(int(line)+1)-1)
else:
    h, order = line.split()
    node = 2**(int(h)+1)-1
    subtract = 0
    state = ''
    if order[0] == 'L':
        subtract = 1
        state = 'L'
    else:
        subtract = 2
        state = 'R'
    node -= subtract
    for i in range(1, len(order)):
        if state == 'L':
            if order[i] == 'L':
                subtract *= 2
            else:
                subtract = subtract * 2 + 1
                state = 'R'
        else:
            if order[i] == 'L':
                subtract = subtract * 2 - 1
                state = 'L'
            else:
                subtract *= 2
        node -= subtract
    print(node)'''
line = input().lstrip()
if line.isdigit():
    print(2**(int(line)+1)-1)
else:
    h, order = line.split()
    ans = 1
    for i in order:
        ans *= 2
        if i == 'R':
            ans += 1
    print(2**(int(h)+1) - ans) 