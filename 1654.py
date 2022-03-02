'''
import sys
ssr = sys.stdin.readline

def count_line(line_len):
    cnt = 0
    for i in line:
        cnt += i//line_len
    return cnt

k,n=map(int, ssr().split())
tmp=n
line=[int(ssr()) for _ in range(k)]
while 1:
    line_len = sum(line)//tmp
    cnt = count_line(line_len)
    if cnt < n:
        tmp+=1
        continue
    else:
        line_len = sum(line)//(tmp-1)
        while 1:
            cnt = count_line(line_len)
            if cnt<n:
                line_len-=1
                continue
            elif cnt == n:
                print(line_len)
                break
        break
'''
import sys
ssr = sys.stdin.readline

k,n = map(int, ssr().split())
line=[int(ssr()) for _ in range(k)]
low = 1
high = sum(line)//n
while low<=high:
    value = (low+high)//2
    cnt = 0
    for i in line:
        cnt += i//value
    if cnt < n:
        high = value-1
    elif cnt >= n:
        low = value+1

print(high)