import sys

num_cnt = [0 for i in range(10000)]
result_list = [0 for i in range(10000)]
n = int(input())
num_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
    num_cnt[num] += 1
for i in range(len(num_cnt)-1):
    num_cnt[i+1] = num_cnt[i]+num_cnt[i+1]
num_list = num_list[::-1]
for i in num_list:
    result_list[num_cnt[i]] = i
    num_cnt[i] -= 1
for i in range(len(result_list)-1):
    if result_list[i] == 0:
        del result_list[i]
    if result_list[i-1] != 0 and result_list[i] == 0:
        result_list = result_list[0:i]
        break
for i in result_list:
    print(i)