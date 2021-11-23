import sys

def get_frequent_num(num : list):
    add_num = abs(min(num))
    for i in range(len(num)):
        num[i] += add_num
    cnt = [0 for i in range(4001+add_num)]
    for i in num:
        cnt[i] += 1
    max_cnt = max(cnt)
    frequent_list = []
    for i in range(len(cnt)):
        if max_cnt == cnt[i]:
            frequent_list.append(i)
    if len(frequent_list) == 1:
        return frequent_list[0]-add_num
    else:
        return frequent_list[1]-add_num
    
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num)/n))
print(num[round(n/2)])
print(get_frequent_num(num))
print(num[n-1]-num[0])