from collections import deque
import sys
ssr = sys.stdin.readline

list = deque()
n = int(ssr())
for i in range(n):
    command = ssr().rstrip()
    if command.find('push_front') != -1:
        list.appendleft(int(command[10:]))
    elif command.find('push_back') != -1:
        list.append(int(command[9:]))
    elif command == 'pop_front':
        if len(list) == 0:
            print(-1)
        else:
            print(list.popleft())
    elif command == 'pop_back':
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop())
    elif command == 'size':
        print(len(list))
    elif command == 'empty':
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif command == 'back':
        if len(list) == 0:
            print(-1)
        else:
            print(list[len(list)-1])
    elif command == 'front':
        if len(list) == 0:
            print(-1)
        else:
            print(list[0])