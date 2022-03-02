import sys
ssr = sys.stdin.readline

n = int(ssr())
list = []
for i in range(n):
    command = ssr().rstrip()
    if command.find('push') != -1:
        list.append(int(command[4:]))
    elif command == 'pop':
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
    elif command == 'top':
        if len(list) == 0:
            print(-1)
        else:
            print(list[len(list)-1])