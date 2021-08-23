import sys

case = int(input())

for i in range(case):
    line = list(map(int,sys.stdin.readline().split()))
    stu = line[0]
    score = line[1:]
    avg=sum(score)/stu
    div_score=[]

    for i in range(stu):
        num=score[i]-avg
        if num>0:
            div_score.append(num)
            
    ratio = len(div_score)/stu
    round_ratio = round(len(div_score)/stu,5)
    str_num = str(int((round_ratio*100000)))
    print(str_num[0]+str_num[1]+'.'+str_num[2]+str_num[3]+str_num[4]+'%')
