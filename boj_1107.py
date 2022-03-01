#작은데서 접근하는 놈이랑 큰데서 접근하는 놈 두 개를 구해야 해
#단 하나라도 다른게 나오면 그 뒤로는 전부 작으면 제일 뒤에거 많으면 제일 앞에거
'''
import sys
ssr = sys.stdin.readline

def make_num(n):
    num = ''
    if btn == []:
        return 100000000
    else:
        for i in range(len(n)):
            k = abs(int(n[i])-btn[0])
            last=btn[0]
            for j in btn:
                if abs(int(n[i])-j)<=k:
                    k = abs(int(n[i])-j)
                    last=j
            num += str(last)
            if n[i]!=num[i]:
                if n[i]> num[i]:
                    for _ in range(len(n)-1-i):
                        num += str(btn[(len(btn)-1)])
                    break
                else:
                    for _ in range(len(n)-1-i):
                        num += str(btn[0])
                    break
    return int(num)

btn = [0,1,2,3,4,5,6,7,8,9]
n = ssr().rstrip()
m = int(ssr())
if m == 0:
    _=0
else:
    b = list(map(int, ssr().split()))
result = abs(int(n)-100)
for i in range(m):
    btn.remove(b[i])
num = make_num(n)
result1 = abs(int(n)-num)+len(str(num))
if result < result1:
    print(result)
else:
    print(result1)
'''

'''
import sys
ssr = sys.stdin.readline

btn = [0,1,2,3,4,5,6,7,8,9]
n = ssr().rstrip()
m = int(ssr())
b = list(map(int, ssr().split()))
for i in range(m):
    btn.remove(b[i])
channel = 100
result = abs(int(n)-channel)
chan=''
for i in btn:
    for _ in range(len(n)):
        chan += str(i)
'''
#사람이라면 이걸 어떻게 풀까
#일단 두 가지의 결과를 비교해야해
#최대한 가까운 번호를 눌러서 채널이동, 쁠마로만 채널 이동
#1.쁠마로만 이동하는 방법 n - 100
#2.최대한 가까운 번호 찾기
#최대한 가까운 번호는 어떻게 찾나?
#일단 첫번째 자리를 최대한 가까운 걸로 찾는다
#같은 경우가 있고 다른 경우가 있다
#같은 경우는 후반 뒷자리만 맞춰주면 되지

n = int(input())
result = abs(100 - n)
m = int(input())
b = input().split()
for i in range(1000001):
    for j in str(i):
        if j in b:
            break
    else:
        result = min(result, len(str(i)) + abs(i - n))
print(result)