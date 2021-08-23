num = int(input())
for i in range(1,num+1):
    line = [' '*(num-i),'*'*i]
    print(''.join(line))