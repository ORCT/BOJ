'''import sys

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
    print(f'{ratio:.3f}%')'''
    
'''
파이썬의 round 메서드의 특성 때문에 틀린다고는 하는거 같던데'''
import sys

ssr = sys.stdin.readline

c = int(ssr())
for _ in range(c):
    n_s = list(map(int, ssr().split()))
    m = sum(n_s[1:])/n_s[0]
    cnt = 0
    for i in range(n_s[0]):
        if n_s[i+1] > m:
            cnt += 1
    ans = cnt/n_s[0]*100*1000
    if ans - int(ans) < 0.5:
        ans = int(ans)
    else:
        ans = int(ans) + 1
    print(f'{str(ans)[:-3]}.{str(ans)[-3:]}%')