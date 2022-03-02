import sys

case = int(input())

for i in range(case):
    line = list(map(int,sys.stdin.readline().split()))
    stu = line[0]
    score = line[1:]
    avg=sum(score)/stu
    count=0

    for i in range(stu):
        num=score[i]-avg
        if num>0:
            count +=1
            
    ratio = count/stu * 100
    print(f'{ratio:.3f}%')