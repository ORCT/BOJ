import sys
case=int(input())
for i in range(case):
    quiz = sys.stdin.readline()
    count_list=[]
    count=0
    for i in range(len(quiz)-1):
        if quiz[i]=='O':
            count=count+1
        elif quiz[i]=='X':
            count=0
        count_list.append(count)
    print(sum(count_list))