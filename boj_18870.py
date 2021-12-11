import sys
ssr = sys.stdin.readline

n = int(ssr())
num = list(map(int, ssr().split()))
sorted_num = sorted(list(set(num)))
dic = {sorted_num[i] : i for i in range(len(sorted_num))}
for i in num:
    print(dic[i], end = ' ')
#만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.