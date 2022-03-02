import sys
ssr = sys.stdin.readline

n = int(ssr())
stack = [0]
stack1 = list(reversed([i for i in range(1,n+1)]))
stack2 = []
main = [int(ssr()) for _ in range(n)]
result = []
for i in main:
    num = i
    if stack[len(stack)-1] < num:
        while stack[len(stack)-1] < num:
            stack.append(stack1.pop())
            result.append('+')
        stack2.append(stack.pop())
        result.append('-')
    elif stack[len(stack)-1] == num:
        while stack[len(stack)-1] == num:
            stack2.append(stack.pop())
            result.append('-')
    else:
        print('NO')
        break

if main == stack2:
    for i in result:
        print(i)